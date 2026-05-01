from django.test import TestCase
from unittest.mock import patch
from datetime import date, time, timedelta
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient
from .models import CompanyProfile, EventType, Event, Booking, CompanyAvailability, CompanyWeekdaySlot

class GoogleCalendarSyncTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.profile = CompanyProfile.get_solo()
        self.category = EventType.objects.create(name="Tours")
        self.service = Event.objects.create(
            event_type=self.category,
            name="Tour",
            price="100.00",
            duration_minutes=60
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
        self.url = reverse('api-bookings')

    @patch('utils.google_calendar.sync_booking_to_google')
    def test_booking_creation_triggers_sync_with_services(self, mock_sync):
        """
        Verify that creating a booking via API triggers Google Calendar sync
        only after services are added, ensuring full data is sent.
        """
        sync_results = []
        def side_effect(booking):
            # Capture state at the time of call
            service_names = ", ".join(s.name for s in booking.services.all())
            sync_results.append({
                "service_count": booking.services.count(),
                "service_names": service_names,
                "google_event_id": booking.google_event_id
            })
            # Simulate updating the event ID on first call
            if not booking.google_event_id:
                Booking.objects.filter(pk=booking.pk).update(google_event_id="mock-event-id")
                booking.google_event_id = "mock-event-id"
        
        mock_sync.side_effect = side_effect
        
        payload = {
            "service_ids": [self.service.id],
            "date": self.tomorrow.strftime('%Y-%m-%d'),
            "startTime": "10:00",
            "clientName": "Test Client",
            "clientEmail": "test@example.com",
            "clientPhone": "123456789"
        }
        
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, 201)
        
        # Should be called exactly once because signals.py skips 'created=True'
        self.assertEqual(len(sync_results), 1, "Should be called exactly once (after services are added)")
        self.assertEqual(sync_results[0]["service_count"], 1)
        self.assertEqual(sync_results[0]["service_names"], "Tour")

    def test_end_time_recalculation_on_save(self):
        """
        Verify that changing start_time correctly updates end_time via the model's save method.
        """
        start_dt = timezone.make_aware(timezone.datetime.combine(self.tomorrow, time(10, 0)))
        booking = Booking.objects.create(
            start_time=start_dt,
            client_name="Test Client",
            client_email="test@example.com"
        )
        booking.services.add(self.service)
        booking.refresh_from_db()
        
        initial_end_time = start_dt + timedelta(minutes=60)
        self.assertEqual(booking.end_time, initial_end_time)
        
        # Change date
        new_start_dt = start_dt + timedelta(days=1)
        booking.start_time = new_start_dt
        booking.save()
        
        booking.refresh_from_db()
        expected_end_time = new_start_dt + timedelta(minutes=60)
        self.assertEqual(booking.end_time, expected_end_time)

    @patch('utils.google_calendar.delete_google_calendar_event')
    def test_booking_deletion_triggers_sync(self, mock_delete):
        """
        Verify that deleting a booking triggers the Google Calendar deletion service.
        """
        booking = Booking.objects.create(
            start_time=timezone.now() + timedelta(days=1),
            client_name="Delete Me",
            client_email="delete@example.com",
            google_event_id="some-id"
        )
        booking.delete()
        mock_delete.assert_called_once_with(booking)

    @patch('utils.google_calendar.sync_booking_to_google')
    def test_booking_update_triggers_sync(self, mock_sync):
        """
        Verify that updating a booking (e.g., status change) triggers a sync.
        """
        booking = Booking.objects.create(
            start_time=timezone.now() + timedelta(days=1),
            client_name="Update Me",
            client_email="update@example.com"
        )
        # First call is skipped (created=True), but let's simulate the second call from m2m
        booking.services.add(self.service)
        self.assertEqual(mock_sync.call_count, 1)
        
        # Now change status
        booking.status = "CONFIRMED"
        booking.save()
        
        # Should be called again for the update
        self.assertEqual(mock_sync.call_count, 2)
