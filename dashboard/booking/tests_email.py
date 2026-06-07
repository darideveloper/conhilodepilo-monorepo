from django.test import TestCase, override_settings
from unittest.mock import patch, MagicMock
from decimal import Decimal
from datetime import date, time, timedelta
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
import stripe
from django.test import TransactionTestCase
from .models import CompanyProfile, EventType, Event, Booking, BookingServiceThrough, AvailabilitySlot
from utils.email import _clean_phone, _build_whatsapp_url, _build_logo_url, send_confirmation_email, send_gift_confirmation_emails


class CleanPhoneTest(TestCase):
    def test_removes_non_digits(self):
        self.assertEqual(_clean_phone("+34 915 23 14 06"), "34915231406")

    def test_removes_dashes_and_parentheses(self):
        self.assertEqual(_clean_phone("(34) 915-23-14-06"), "34915231406")

    def test_returns_empty_for_none(self):
        self.assertEqual(_clean_phone(None), "")

    def test_returns_empty_for_empty_string(self):
        self.assertEqual(_clean_phone(""), "")

    def test_preserves_digits_only(self):
        self.assertEqual(_clean_phone("915231406"), "915231406")


class BuildWhatsAppUrlTest(TestCase):
    def test_returns_url_for_valid_phone(self):
        url = _build_whatsapp_url("+34 915 23 14 06")
        self.assertEqual(url, "https://wa.me/34915231406")

    def test_returns_none_for_none(self):
        self.assertIsNone(_build_whatsapp_url(None))

    def test_returns_none_for_empty(self):
        self.assertIsNone(_build_whatsapp_url(""))


class BuildLogoUrlTest(TestCase):
    @override_settings(HOST="https://dashboard.conhilodepilo.com")
    def test_returns_absolute_url_when_logo_exists(self):
        company = MagicMock(spec=CompanyProfile)
        company.logo.url = "/media/branding/logo.png"
        company.logo.__bool__ = lambda self: True
        url = _build_logo_url(company)
        self.assertEqual(url, "https://dashboard.conhilodepilo.com/media/branding/logo.png")

    @override_settings(HOST="https://dashboard.conhilodepilo.com/")
    def test_strips_trailing_slash_from_host(self):
        company = MagicMock(spec=CompanyProfile)
        company.logo.url = "/media/branding/logo.png"
        company.logo.__bool__ = lambda self: True
        url = _build_logo_url(company)
        self.assertEqual(url, "https://dashboard.conhilodepilo.com/media/branding/logo.png")

    def test_returns_none_when_no_logo(self):
        company = MagicMock(spec=CompanyProfile)
        company.logo = None
        url = _build_logo_url(company)
        self.assertIsNone(url)

    @override_settings(HOST="")
    def test_returns_none_when_no_host(self):
        company = MagicMock(spec=CompanyProfile)
        company.logo.url = "/media/branding/logo.png"
        company.logo.__bool__ = lambda self: True
        url = _build_logo_url(company)
        self.assertIsNone(url)


@override_settings(
    EMAIL_FROM="test@conhilodepilo.com",
    EMAILS_NOTIFICATIONS=["admin@conhilodepilo.com", "notifications@conhilodepilo.com"],
    HOST="https://dashboard.conhilodepilo.localhost",
)
class SendConfirmationEmailTest(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(name="Test Type")
        self.event = Event.objects.create(
            event_type=self.event_type,
            name="Depilación Cejas",
            price=Decimal("15.00"),
            duration_minutes=20,
        )
        self.booking = Booking.objects.create(
            client_name="Cliente Test",
            client_email="cliente@example.com",
            client_phone="+34 666 123 456",
            status="CONFIRMED",
            start_time=timezone.make_aware(
                timezone.datetime(2026, 6, 10, 10, 0)
            ),
        )
        BookingServiceThrough.objects.create(
            booking=self.booking, event=self.event, quantity=1, unit_price=self.event.price
        )

    def test_sends_email_to_client_with_bcc_to_admins(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance

            send_confirmation_email(self.booking)

            mock_email_cls.assert_called_once()
            call_kwargs = mock_email_cls.call_args.kwargs
            self.assertEqual(call_kwargs["to"], ["cliente@example.com"])
            self.assertEqual(
                call_kwargs["bcc"],
                ["admin@conhilodepilo.com", "notifications@conhilodepilo.com"],
            )
            self.assertIn("Confirmación de tu cita", call_kwargs["subject"])
            self.assertIn("Con Hilo Depilo", call_kwargs["subject"])
            mock_instance.attach_alternative.assert_called_once()
            html_arg = mock_instance.attach_alternative.call_args[0][0]
            self.assertIn("cliente@example.com", call_kwargs["to"])

    def test_plain_text_body_contains_booking_details(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance

            send_confirmation_email(self.booking)

            call_kwargs = mock_email_cls.call_args.kwargs
            body = call_kwargs["body"]
            self.assertIn("Cliente Test", body)
            self.assertIn("Depilación Cejas", body)
            self.assertIn("×1", body)
            self.assertIn("15.00", body)
            self.assertIn("10/06/2026", body)
            self.assertIn("10:00", body)

    def test_plain_text_body_contains_pricing_summary(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance

            send_confirmation_email(self.booking)

            call_kwargs = mock_email_cls.call_args.kwargs
            body = call_kwargs["body"]
            self.assertIn("Subtotal", body)
            self.assertIn("Total", body)

    def test_html_alternative_is_attached(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance

            send_confirmation_email(self.booking)

            mock_instance.attach_alternative.assert_called_once()
            args, kwargs = mock_instance.attach_alternative.call_args
            self.assertEqual(args[1], "text/html")
            self.assertIn("Hola, Cliente Test", args[0])

    @override_settings(EMAILS_NOTIFICATIONS=["", "admin@test.com", "  "])
    def test_filters_empty_bcc_emails(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance

            send_confirmation_email(self.booking)

            call_kwargs = mock_email_cls.call_args.kwargs
            self.assertEqual(call_kwargs["bcc"], ["admin@test.com"])

    def test_failure_is_caught_and_logged(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_instance.send.side_effect = Exception("SMTP connection refused")
            mock_email_cls.return_value = mock_instance

            with patch("utils.email.logger") as mock_logger:
                # Should not raise
                send_confirmation_email(self.booking)

                mock_logger.exception.assert_called_once()


@override_settings(
    STRIPE_SECRET_KEY="sk_test_123",
    STRIPE_WEBHOOK_SECRET="whsec_test",
    LANDING_URL="http://test-landing.com",
    EMAIL_FROM="test@conhilodepilo.com",
    EMAILS_NOTIFICATIONS=[],
    HOST="https://dashboard.conhilodepilo.localhost",
)
class EmailSentOnCreateBookingViewTest(TransactionTestCase):
    client_class = APIClient
    def setUp(self):
        CompanyProfile.get_solo()
        self.event_type = EventType.objects.create(
            name="Test Type", payment_model="POST-PAID"
        )
        self.event = Event.objects.create(
            event_type=self.event_type,
            name="Depilación Cejas",
            price=Decimal("15.00"),
            duration_minutes=20,
        )
        AvailabilitySlot.objects.create(
            event=self.event, weekday=0,
            start_time="09:00", end_time="18:00"
        )

    @patch("booking.views.send_confirmation_email")
    def test_email_sent_when_booking_created_as_confirmed(self, mock_send_email):
        response = self.client.post(
            reverse("api-bookings"),
            {
                "services": [{"service_id": self.event.id, "quantity": 1}],
                "date": "2026-06-15",
                "startTime": "10:00",
                "clientName": "Test Client",
                "clientEmail": "test@example.com",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        mock_send_email.assert_called_once()
        booking = mock_send_email.call_args[0][0]
        self.assertEqual(booking.client_name, "Test Client")
        self.assertEqual(booking.client_email, "test@example.com")

    @patch("utils.email.EmailMultiAlternatives")
    def test_email_failure_does_not_block_booking_creation(self, mock_email_cls):
        mock_instance = MagicMock()
        mock_instance.send.side_effect = Exception("SMTP connection refused")
        mock_email_cls.return_value = mock_instance
        response = self.client.post(
            reverse("api-bookings"),
            {
                "services": [{"service_id": self.event.id, "quantity": 1}],
                "date": "2026-06-15",
                "startTime": "10:00",
                "clientName": "Test Client",
                "clientEmail": "test@example.com",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        booking_id = response.json()["booking_id"]
        booking = Booking.objects.get(id=booking_id)
        self.assertEqual(booking.status, "CONFIRMED")


@override_settings(
    STRIPE_SECRET_KEY="sk_test_123",
    STRIPE_WEBHOOK_SECRET="whsec_test",
    LANDING_URL="http://test-landing.com",
    EMAIL_FROM="test@conhilodepilo.com",
    EMAILS_NOTIFICATIONS=[],
    HOST="https://dashboard.conhilodepilo.localhost",
)
class EmailSentOnStripeWebhookTest(TransactionTestCase):
    client_class = APIClient
    def setUp(self):
        CompanyProfile.get_solo()
        self.event_type = EventType.objects.create(
            name="Test Type", payment_model="PRE-PAID"
        )
        self.event = Event.objects.create(
            event_type=self.event_type,
            name="Depilación Cejas",
            price=Decimal("15.00"),
            duration_minutes=20,
        )
    @patch("booking.views.send_confirmation_email")
    @patch("stripe.Webhook.construct_event")
    def test_email_sent_when_booking_transitions_to_paid(
        self, mock_construct_event, mock_send_email
    ):
        booking = Booking.objects.create(
            client_name="Stripe Client",
            client_email="stripe@example.com",
            status="PENDING",
            start_time=timezone.make_aware(
                timezone.datetime(2026, 6, 15, 10, 0)
            ),
        )
        BookingServiceThrough.objects.create(
            booking=booking, event=self.event, quantity=1, unit_price=self.event.price
        )
        mock_event = MagicMock()
        mock_event.id = "evt_test_123"
        mock_event.type = "checkout.session.completed"
        mock_event.data.object.metadata = MagicMock()
        mock_event.data.object.metadata.booking_id = str(booking.id)
        mock_event.data.object.payment_intent = "pi_test_123"
        mock_event.data.object.id = "cs_test_123"
        mock_construct_event.return_value = mock_event

        response = self.client.post(
            reverse("stripe-webhook"),
            data="{}",
            content_type="application/json",
            HTTP_STRIPE_SIGNATURE="test_sig",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        booking.refresh_from_db()
        self.assertEqual(booking.status, "PAID")
        mock_send_email.assert_called_once()
        called_booking = mock_send_email.call_args[0][0]
        self.assertEqual(called_booking.id, booking.id)


@override_settings(
    EMAIL_FROM="test@conhilodepilo.com",
    EMAILS_NOTIFICATIONS=["admin@conhilodepilo.com", "notifications@conhilodepilo.com"],
    HOST="https://dashboard.conhilodepilo.localhost",
)
class GiftEmailTest(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(name="Test Type")
        self.event = Event.objects.create(
            event_type=self.event_type,
            name="Depilación Cejas",
            price=Decimal("15.00"),
            duration_minutes=20,
        )
        self.booking = Booking.objects.create(
            client_name="Bob Recipient",
            client_email="bob@example.com",
            client_phone="+34 666 123 456",
            is_gift=True,
            buyer_name="Alice Buyer",
            buyer_email="alice@example.com",
            recipient_name="Bob Recipient",
            recipient_email="bob@example.com",
            status="CONFIRMED",
            start_time=timezone.make_aware(
                timezone.datetime(2026, 6, 10, 10, 0)
            ),
        )
        BookingServiceThrough.objects.create(
            booking=self.booking, event=self.event, quantity=1, unit_price=self.event.price
        )

    def test_sends_two_emails(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance
            send_gift_confirmation_emails(self.booking)
            self.assertEqual(mock_email_cls.call_count, 2)

    def test_recipient_email_sent_first_with_gift_context(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance
            send_gift_confirmation_emails(self.booking)
            first_call = mock_email_cls.call_args_list[0]
            kwargs = first_call.kwargs
            self.assertEqual(kwargs["to"], ["bob@example.com"])
            self.assertIn("Has recibido un regalo de Alice Buyer", kwargs["subject"])

    def test_buyer_email_sent_second_with_gift_context(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance
            send_gift_confirmation_emails(self.booking)
            second_call = mock_email_cls.call_args_list[1]
            kwargs = second_call.kwargs
            self.assertEqual(kwargs["to"], ["alice@example.com"])
            self.assertIn("Has regalado una cita a Bob Recipient", kwargs["subject"])

    def test_both_emails_include_bcc_to_admins(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance
            send_gift_confirmation_emails(self.booking)
            for call_args in mock_email_cls.call_args_list:
                kwargs = call_args.kwargs
                self.assertIn("admin@conhilodepilo.com", kwargs["bcc"])
                self.assertIn("notifications@conhilodepilo.com", kwargs["bcc"])

    def test_html_alternative_attached_to_both_emails(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_email_cls.return_value = mock_instance
            send_gift_confirmation_emails(self.booking)
            self.assertEqual(mock_instance.attach_alternative.call_count, 2)

    def test_failure_of_one_email_does_not_block_other(self):
        with patch("utils.email.EmailMultiAlternatives") as mock_email_cls:
            mock_instance = MagicMock()
            mock_instance.send.side_effect = [Exception("SMTP error"), None]
            mock_email_cls.return_value = mock_instance
            with patch("utils.email.logger") as mock_logger:
                send_gift_confirmation_emails(self.booking)
                self.assertEqual(mock_logger.exception.call_count, 1)
                self.assertEqual(mock_email_cls.call_count, 2)
