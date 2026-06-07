from decimal import Decimal
from datetime import date, time, timedelta
from unittest.mock import patch, MagicMock
from django.test import TestCase, TransactionTestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from .models import (
    CompanyProfile, EventType, Event, Booking,
    BookingServiceThrough, CompanyAvailability,
    CompanyWeekdaySlot
)


class BookingServiceThroughTest(APITestCase):
    """Covers 11.4: Test for BookingServiceThrough creation with quantities."""

    def setUp(self):
        self.profile = CompanyProfile.get_solo()
        self.category = EventType.objects.create(name="Test Category", payment_model="POST-PAID")
        self.service = Event.objects.create(
            event_type=self.category,
            name="Test Service",
            price=Decimal("50.00"),
            duration_minutes=30,
            buy_x=0,
            get_y_free=0
        )
        self.tomorrow = date.today() + timedelta(days=1)
        CompanyAvailability.objects.create(
            company=self.profile,
            start_date=self.tomorrow,
            end_date=self.tomorrow + timedelta(days=7)
        )
        CompanyWeekdaySlot.objects.create(
            company=self.profile,
            weekday=self.tomorrow.weekday(),
            start_time=time(9, 0),
            end_time=time(17, 0)
        )
        self.url = reverse("api-bookings")

    def test_through_model_creation_with_quantity(self):
        payload = {
            "services": [{"service_id": self.service.id, "quantity": 3}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Qty Test",
            "clientEmail": "qty@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)

        booking = Booking.objects.get(client_email="qty@example.com")
        through_rows = BookingServiceThrough.objects.filter(booking=booking)
        self.assertEqual(through_rows.count(), 1)
        through = through_rows.first()
        self.assertEqual(through.quantity, 3)
        self.assertEqual(through.unit_price, Decimal("50.00"))
        self.assertEqual(through.event, self.service)

    def test_through_model_multiple_services(self):
        service2 = Event.objects.create(
            event_type=self.category,
            name="Service B",
            price=Decimal("30.00"),
            duration_minutes=20,
            buy_x=0,
            get_y_free=0
        )
        payload = {
            "services": [
                {"service_id": self.service.id, "quantity": 2},
                {"service_id": service2.id, "quantity": 1},
            ],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Multi Service",
            "clientEmail": "multi@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)

        booking = Booking.objects.get(client_email="multi@example.com")
        through_rows = BookingServiceThrough.objects.filter(booking=booking).order_by("event_id")
        self.assertEqual(through_rows.count(), 2)
        self.assertEqual(through_rows[0].quantity, 2)
        self.assertEqual(through_rows[0].unit_price, Decimal("50.00"))
        self.assertEqual(through_rows[1].quantity, 1)
        self.assertEqual(through_rows[1].unit_price, Decimal("30.00"))


class CreateBookingWithPromotionsTest(APITestCase):
    """Covers 11.2: Test for CreateBookingView with quantities and promotions."""

    def setUp(self):
        self.profile = CompanyProfile.get_solo()
        self.category = EventType.objects.create(name="Test Category", payment_model="POST-PAID")
        self.service = Event.objects.create(
            event_type=self.category,
            name="Promo Service",
            price=Decimal("30.00"),
            duration_minutes=30,
            buy_x=2,
            get_y_free=1
        )
        self.tomorrow = date.today() + timedelta(days=1)
        CompanyAvailability.objects.create(
            company=self.profile,
            start_date=self.tomorrow,
            end_date=self.tomorrow + timedelta(days=7)
        )
        CompanyWeekdaySlot.objects.create(
            company=self.profile,
            weekday=self.tomorrow.weekday(),
            start_time=time(9, 0),
            end_time=time(17, 0)
        )
        self.url = reverse("api-bookings")

    def test_booking_with_promotion_discount(self):
        payload = {
            "services": [{"service_id": self.service.id, "quantity": 3}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Promo User",
            "clientEmail": "promo@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(Decimal(data["original_amount"]), Decimal("90.00"))
        self.assertEqual(Decimal(data["discount_amount"]), Decimal("30.00"))
        self.assertEqual(Decimal(data["total_amount"]), Decimal("60.00"))

    def test_booking_without_promotion(self):
        payload = {
            "services": [{"service_id": self.service.id, "quantity": 1}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "No Promo",
            "clientEmail": "nopromo@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(Decimal(data["original_amount"]), Decimal("30.00"))
        self.assertEqual(Decimal(data["discount_amount"]), Decimal("0.00"))
        self.assertEqual(Decimal(data["total_amount"]), Decimal("30.00"))

    @override_settings(
        STRIPE_SECRET_KEY="sk_test_123",
        STRIPE_WEBHOOK_SECRET="whsec_123",
        LANDING_URL="http://test-landing.com"
    )
    @patch("utils.stripe_utils.stripe.checkout.Session.create")
    def test_pre_paid_with_promotion_stripe_amount(self, mock_session_create):
        self.category.payment_model = "PRE-PAID"
        self.category.save()

        mock_session = MagicMock()
        mock_session.url = "https://checkout.stripe.com/pay/cs_test"
        mock_session_create.return_value = mock_session

        payload = {
            "services": [{"service_id": self.service.id, "quantity": 3}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Stripe Promo",
            "clientEmail": "stripepromo@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertTrue(data["payment_required"])
        self.assertEqual(data["checkout_url"], "https://checkout.stripe.com/pay/cs_test")

        mock_session_create.assert_called_once()
        kwargs = mock_session_create.call_args[1]
        self.assertEqual(kwargs["line_items"][0]["price_data"]["unit_amount"], 6000)

    def test_quantity_validation_rejects_zero(self):
        payload = {
            "services": [{"service_id": self.service.id, "quantity": 0}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Bad Qty",
            "clientEmail": "badqty@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("quantity must be at least 1", response.json()["error"])

    def test_quantity_validation_rejects_negative(self):
        payload = {
            "services": [{"service_id": self.service.id, "quantity": -1}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Neg Qty",
            "clientEmail": "negqty@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 400)


class AvailabilityWithQuantitiesTest(APITestCase):
    """Covers 11.3: Test for availability endpoints with quantities parameter."""

    def setUp(self):
        self.profile = CompanyProfile.get_solo()
        self.days_url = reverse("api-availability-days")
        self.slots_url = reverse("api-availability-slots")

        self.category = EventType.objects.create(name="Test Category")
        self.service = Event.objects.create(
            event_type=self.category,
            name="Availability Test",
            price=Decimal("30.00"),
            duration_minutes=30,
            buy_x=0,
            get_y_free=0
        )
        self.today = date.today()
        self.tomorrow = self.today + timedelta(days=1)

        CompanyAvailability.objects.create(
            company=self.profile,
            start_date=self.tomorrow,
            end_date=self.tomorrow + timedelta(days=30)
        )
        CompanyWeekdaySlot.objects.create(
            company=self.profile,
            weekday=self.tomorrow.weekday(),
            start_time=time(9, 0),
            end_time=time(17, 0)
        )

    def test_days_with_quantities(self):
        response = self.client.get(
            self.days_url,
            {"service_ids": str(self.service.id), "quantities": "3"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.tomorrow.strftime("%Y-%m-%d"), response.json())

    def test_slots_with_quantities(self):
        response = self.client.get(
            self.slots_url,
            {
                "service_ids": str(self.service.id),
                "quantities": "3",
                "date": self.tomorrow.strftime("%Y-%m-%d"),
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_quantities_length_mismatch(self):
        response = self.client.get(
            self.days_url,
            {"service_ids": "1,2", "quantities": "3"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("quantities length must match", response.json()["error"])

    def test_quantities_invalid_value(self):
        response = self.client.get(
            self.slots_url,
            {
                "service_ids": str(self.service.id),
                "quantities": "-1",
                "date": self.tomorrow.strftime("%Y-%m-%d"),
            }
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("quantities must be positive", response.json()["error"])

    def test_slots_without_quantities_defaults_to_1(self):
        response = self.client.get(
            self.slots_url,
            {
                "service_ids": str(self.service.id),
                "date": self.tomorrow.strftime("%Y-%m-%d"),
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)


class PriceSnapshotTest(APITestCase):
    """Covers 11.6: Test that booking price snapshots remain unchanged when the
    underlying Event price changes after booking creation."""

    def setUp(self):
        self.profile = CompanyProfile.get_solo()
        self.category = EventType.objects.create(name="Test Category", payment_model="POST-PAID")
        self.service = Event.objects.create(
            event_type=self.category,
            name="Snapshot Service",
            price=Decimal("100.00"),
            duration_minutes=60,
            buy_x=0,
            get_y_free=0
        )
        self.tomorrow = date.today() + timedelta(days=1)
        CompanyAvailability.objects.create(
            company=self.profile,
            start_date=self.tomorrow,
            end_date=self.tomorrow + timedelta(days=7)
        )
        CompanyWeekdaySlot.objects.create(
            company=self.profile,
            weekday=self.tomorrow.weekday(),
            start_time=time(9, 0),
            end_time=time(17, 0)
        )
        self.url = reverse("api-bookings")

    def test_price_snapshot_preserved_after_event_price_change(self):
        payload = {
            "services": [{"service_id": self.service.id, "quantity": 2}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Snapshot User",
            "clientEmail": "snapshot@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(Decimal(data["original_amount"]), Decimal("200.00"))

        self.service.price = Decimal("150.00")
        self.service.save()

        booking = Booking.objects.get(client_email="snapshot@example.com")
        self.assertEqual(booking.original_amount, Decimal("200.00"))
        self.assertEqual(booking.total_amount, Decimal("200.00"))

        through = BookingServiceThrough.objects.get(booking=booking)
        self.assertEqual(through.unit_price, Decimal("100.00"))


@override_settings(
    STRIPE_SECRET_KEY="sk_test_123",
    STRIPE_WEBHOOK_SECRET="whsec_123",
    LANDING_URL="http://test-landing.com"
)
class ZeroTotalBookingTest(APITestCase):
    """Covers 11.7: Test that PRE-PAID bookings discounted to total_amount=0
    skip Stripe and return payment_required: false."""

    def setUp(self):
        self.profile = CompanyProfile.get_solo()
        self.category = EventType.objects.create(name="Free Prepaid", payment_model="PRE-PAID")
        self.service = Event.objects.create(
            event_type=self.category,
            name="Free Service",
            price=Decimal("0.00"),
            duration_minutes=30,
            buy_x=0,
            get_y_free=0
        )
        self.tomorrow = date.today() + timedelta(days=1)
        CompanyAvailability.objects.create(
            company=self.profile,
            start_date=self.tomorrow,
            end_date=self.tomorrow + timedelta(days=7)
        )
        CompanyWeekdaySlot.objects.create(
            company=self.profile,
            weekday=self.tomorrow.weekday(),
            start_time=time(9, 0),
            end_time=time(17, 0)
        )
        self.url = reverse("api-bookings")

    def test_zero_total_pre_paid_skips_stripe(self):
        payload = {
            "services": [{"service_id": self.service.id, "quantity": 1}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Zero Total",
            "clientEmail": "zero@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertFalse(data["payment_required"])
        self.assertNotIn("checkout_url", data)

        booking = Booking.objects.get(client_email="zero@example.com")
        self.assertEqual(booking.status, "PENDING")

    @patch("utils.stripe_utils.stripe.checkout.Session.create")
    def test_promotion_discount_to_zero_skips_stripe(self, mock_session_create):
        promo_service = Event.objects.create(
            event_type=self.category,
            name="Promo to Free",
            price=Decimal("30.00"),
            duration_minutes=30,
            buy_x=1,
            get_y_free=1
        )
        payload = {
            "services": [{"service_id": promo_service.id, "quantity": 1}],
            "date": self.tomorrow.strftime("%Y-%m-%d"),
            "startTime": "10:00",
            "clientName": "Promo To Zero",
            "clientEmail": "promozero@example.com",
        }
        response = self.client.post(self.url, payload, format="json")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertFalse(data["payment_required"])
        self.assertNotIn("checkout_url", data)
        mock_session_create.assert_not_called()
