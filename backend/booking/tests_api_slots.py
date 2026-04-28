from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from datetime import date, time, datetime
from booking.models import EventType, Event, AvailabilitySlot, Booking
from django.utils import timezone

class AvailabilitySlotsApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = EventType.objects.create(name="Beauty", allow_overlap=False)
        self.service = Event.objects.create(
            event_type=self.category,
            name="Service 1",
            price="50.00",
            duration_minutes=30
        )
        # Monday slots: 09:00 - 11:00
        AvailabilitySlot.objects.create(event=self.service, weekday=0, start_time="09:00:00", end_time="11:00:00")

    def test_get_slots_success(self):
        """
        Verify that slots are generated correctly with 15-min intervals.
        """
        target_date = "2026-06-01" # Monday
        url = reverse('api-availability-slots')
        response = self.client.get(url, {'service_ids': self.service.id, 'date': target_date})
        
        self.assertEqual(response.status_code, 200)
        # 09:00, 09:15, 09:30, 09:45, 10:00, 10:15, 10:30
        # 10:30 + 30m = 11:00. 10:45 + 30m = 11:15 (too late).
        expected_slots = ["09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30"]
        self.assertEqual(response.data, expected_slots)

    def test_get_slots_with_booking(self):
        """
        Verify that slots overlapping with a booking are excluded.
        """
        target_date_str = "2026-06-01"
        target_date = date(2026, 6, 1)
        
        # Book 09:15 to 09:45 (30m)
        start_time = timezone.make_aware(datetime.combine(target_date, time(9, 15)))
        booking = Booking.objects.create(
            client_name="Test",
            client_email="test@test.com",
            start_time=start_time,
            status="CONFIRMED"
        )
        booking.services.add(self.service)
        
        url = reverse('api-availability-slots')
        response = self.client.get(url, {'service_ids': self.service.id, 'date': target_date_str})
        
        # Original: 09:00, 09:15, 09:30, 09:45, 10:00, 10:15, 10:30
        # Booked: 09:15-09:45.
        # 09:00 + 30m = 09:30 (overlaps 09:15-09:45). NO.
        # 09:15 + 30m = 09:45 (overlaps). NO.
        # 09:30 + 30m = 10:00 (overlaps). NO.
        # 09:45 + 30m = 10:15 (free). YES.
        # 10:00, 10:15, 10:30. YES.
        
        expected_slots = ["09:45", "10:00", "10:15", "10:30"]
        self.assertEqual(response.data, expected_slots)

    def test_overlap_slots(self):
        """
        Verify that slots are not excluded if overlap is allowed.
        """
        self.category.allow_overlap = True
        self.category.save()
        
        target_date_str = "2026-06-01"
        target_date = date(2026, 6, 1)
        
        # Book 09:00 to 10:00
        start_time = timezone.make_aware(datetime.combine(target_date, time(9, 0)))
        booking = Booking.objects.create(
            client_name="Test",
            client_email="test@test.com",
            start_time=start_time,
            status="CONFIRMED"
        )
        booking.services.add(self.service)
        booking.services.add(self.service) # 2x30m = 1h
        
        url = reverse('api-availability-slots')
        response = self.client.get(url, {'service_ids': self.service.id, 'date': target_date_str})
        
        # Should return all slots as if no booking existed
        expected_slots = ["09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30"]
        self.assertEqual(response.data, expected_slots)
