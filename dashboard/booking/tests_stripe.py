from django.test import TestCase, override_settings
from unittest.mock import patch, MagicMock
from decimal import Decimal
from datetime import date, time, timedelta
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient
import stripe
from .models import CompanyProfile, EventType, Event, Booking

@override_settings(STRIPE_SECRET_KEY="sk_test_123", STRIPE_WEBHOOK_SECRET="whsec_123", LANDING_URL="http://test-landing.com")
class StripeIntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.profile = CompanyProfile.get_solo()
        self.profile.currency = "EUR"
        self.profile.save()

        self.category = EventType.objects.create(name="Tours", payment_model="PRE-PAID")
        self.service = Event.objects.create(
            event_type=self.category,
            name="Prepaid Tour",
            price=Decimal("150.50"),
            duration_minutes=60
        )
        
        self.post_paid_category = EventType.objects.create(name="Consultations", payment_model="POST-PAID")
        self.post_paid_service = Event.objects.create(
            event_type=self.post_paid_category,
            name="Free Consult",
            price=Decimal("0.00"),
            duration_minutes=30
        )

        self.tomorrow = date.today() + timedelta(days=1)
        # Mock availability for tomorrow
        from .models import CompanyAvailability, CompanyWeekdaySlot
        CompanyAvailability.objects.create(company=self.profile, start_date=self.tomorrow, end_date=self.tomorrow)
        CompanyWeekdaySlot.objects.create(
            company=self.profile, 
            weekday=self.tomorrow.weekday(), 
            start_time=time(9, 0), 
            end_time=time(17, 0)
        )

    @patch('utils.stripe_utils.stripe.checkout.Session.create')
    def test_create_booking_with_stripe_redirect(self, mock_session_create):
        """
        Verify that a booking with PRE-PAID services triggers Stripe session creation
        and returns a checkout URL.
        """
        mock_session = MagicMock()
        mock_session.url = "https://checkout.stripe.com/pay/cs_test_123"
        mock_session_create.return_value = mock_session

        url = reverse('api-bookings')
        payload = {
            "service_ids": [self.service.id],
            "date": self.tomorrow.strftime('%Y-%m-%d'),
            "startTime": "10:00",
            "clientName": "Stripe User",
            "clientEmail": "stripe@example.com"
        }

        response = self.client.post(url, payload, format='json')
        
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertTrue(data['payment_required'])
        self.assertEqual(data['checkout_url'], "https://checkout.stripe.com/pay/cs_test_123")
        
        # Verify multiplier (150.50 * 100 = 15050)
        mock_session_create.assert_called_once()
        args, kwargs = mock_session_create.call_args
        self.assertEqual(kwargs['line_items'][0]['price_data']['unit_amount'], 15050)
        self.assertEqual(kwargs['success_url'], "http://test-landing.com/success?session_id={CHECKOUT_SESSION_ID}")

    def test_create_booking_post_paid_skips_stripe(self):
        """
        Verify that a booking with only POST-PAID services is confirmed immediately.
        """
        url = reverse('api-bookings')
        payload = {
            "service_ids": [self.post_paid_service.id],
            "date": self.tomorrow.strftime('%Y-%m-%d'),
            "startTime": "11:00",
            "clientName": "Regular User",
            "clientEmail": "regular@example.com"
        }

        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertFalse(data['payment_required'])
        self.assertNotIn('checkout_url', data)
        
        # Verify status in DB
        booking = Booking.objects.get(client_email="regular@example.com")
        self.assertEqual(booking.status, "CONFIRMED")

    @patch('stripe.Webhook.construct_event')
    def test_webhook_successful_payment(self, mock_construct_event):
        """
        Verify that a successful payment webhook updates the booking status to PAID.
        """
        booking = Booking.objects.create(
            start_time=timezone.now(),
            client_name="Webhook Test",
            client_email="webhook@example.com",
            status="PENDING"
        )
        
        # Mock Stripe event
        mock_construct_event.return_value = {
            'type': 'checkout.session.completed',
            'data': {
                'object': {
                    'metadata': {'booking_id': str(booking.id)},
                    'payment_intent': 'pi_test_123'
                }
            }
        }

        url = reverse('stripe-webhook')
        response = self.client.post(url, data={}, HTTP_STRIPE_SIGNATURE="mock_sig")
        
        self.assertEqual(response.status_code, 200)
        booking.refresh_from_db()
        self.assertEqual(booking.status, "PAID")
        self.assertEqual(booking.stripe_payment_id, "pi_test_123")

    @patch('stripe.Webhook.construct_event')
    def test_webhook_invalid_signature(self, mock_construct_event):
        """
        Verify that webhooks with invalid signatures are rejected.
        """
        mock_construct_event.side_effect = stripe.error.SignatureVerificationError("Invalid", "sig")
        
        url = reverse('stripe-webhook')
        response = self.client.post(url, data={}, HTTP_STRIPE_SIGNATURE="invalid_sig")
        
        self.assertEqual(response.status_code, 400)
