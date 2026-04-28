from django.test import TestCase
from datetime import date, timedelta, time, datetime
from booking.models import CompanyProfile, EventType, Event, EventAvailability, EventDateOverride, AvailabilitySlot, Booking
from utils.availability import get_available_dates
from django.db import reset_queries
from django.utils import timezone

class AvailabilityIntersectionTest(TestCase):
    def setUp(self):
        self.category = EventType.objects.create(name="Beauty")
        
        # Service A: available 2026-01-01 to 2026-01-10
        self.service_a = Event.objects.create(
            event_type=self.category,
            name="Service A",
            price="50.00",
            duration_minutes=30
        )
        EventAvailability.objects.create(
            event=self.service_a,
            start_date=date(2026, 1, 1),
            end_date=date(2026, 1, 10)
        )
        # Service A also has an override for 2026-01-15 (making it available when otherwise it wouldn't be)
        EventDateOverride.objects.create(
            event=self.service_a,
            date=date(2026, 1, 15),
            is_available=True,
            start_time="09:00:00",
            end_time="17:00:00"
        )

        # Service B: available 2026-01-05 to 2026-02-10
        self.service_b = Event.objects.create(
            event_type=self.category,
            name="Service B",
            price="60.00",
            duration_minutes=45
        )
        EventAvailability.objects.create(
            event=self.service_b,
            start_date=date(2026, 1, 5),
            end_date=date(2026, 2, 10)
        )
        
        # Add weekday slots for both to be available on all days within their ranges
        for i in range(7):
            AvailabilitySlot.objects.create(event=self.service_a, weekday=i, start_time="09:00:00", end_time="17:00:00")
            AvailabilitySlot.objects.create(event=self.service_b, weekday=i, start_time="09:00:00", end_time="17:00:00")

    def test_intersection_logic(self):
        """
        Verify that the returned dates are only the intersection of all validations.
        """
        service_ids = [self.service_a.id, self.service_b.id]
        available_dates = get_available_dates(service_ids, start_date=date(2026, 1, 1))
        
        expected_dates = [(date(2026, 1, 5) + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6)]
        self.assertEqual(available_dates, expected_dates)
        self.assertNotIn("2026-01-15", available_dates)

    def test_query_count_optimization(self):
        """
        Verify that the number of queries is constant and not N+1.
        """
        service_ids = [self.service_a.id, self.service_b.id]
        reset_queries()
        
        # We expect a constant number of queries.
        with self.assertNumQueries(10):
            get_available_dates(service_ids, start_date=date(2026, 1, 1))

class BookingConflictTest(TestCase):
    def setUp(self):
        self.category_private = EventType.objects.create(name="Private", allow_overlap=False)
        self.category_overlap = EventType.objects.create(name="Group", allow_overlap=True)
        
        self.service_private = Event.objects.create(
            event_type=self.category_private,
            name="Private Service",
            price="100.00",
            duration_minutes=60
        )
        self.service_short = Event.objects.create(
            event_type=self.category_private,
            name="Short Service",
            price="50.00",
            duration_minutes=30
        )
        self.service_overlap = Event.objects.create(
            event_type=self.category_overlap,
            name="Group Service",
            price="20.00",
            duration_minutes=60
        )
        
        # Available from 09:00 to 11:00 (2 hours)
        for i in range(7):
            AvailabilitySlot.objects.create(event=self.service_private, weekday=i, start_time="09:00:00", end_time="11:00:00")
            AvailabilitySlot.objects.create(event=self.service_short, weekday=i, start_time="09:00:00", end_time="11:00:00")
            AvailabilitySlot.objects.create(event=self.service_overlap, weekday=i, start_time="09:00:00", end_time="11:00:00")

    def test_strict_conflict(self):
        """
        Private service should be unavailable if the remaining window is too small.
        """
        target_date = date(2026, 6, 1) # a Monday
        
        # Book 09:30 to 10:30 (leaves two 30-min windows: 09:00-09:30 and 10:30-11:00)
        start_time = timezone.make_aware(datetime.combine(target_date, time(9, 30)))
        booking = Booking.objects.create(
            client_name="Test",
            client_email="test@test.com",
            start_time=start_time,
            status="CONFIRMED"
        )
        booking.services.add(self.service_private) # 60 mins
        
        # Service Private needs 60 mins. 
        # Neither 30-min window is enough.
        available_dates = get_available_dates([self.service_private.id], start_date=target_date)
        self.assertNotIn(target_date.strftime('%Y-%m-%d'), available_dates)

    def test_overlap_allowed(self):
        """
        Group service should be available even if someone else booked the same slot.
        """
        target_date = date(2026, 6, 1)
        
        # Book 09:00 to 11:00 (full day)
        start_time = timezone.make_aware(datetime.combine(target_date, time(9, 0)))
        booking = Booking.objects.create(
            client_name="Test",
            client_email="test@test.com",
            start_time=start_time,
            status="CONFIRMED"
        )
        # Add two 60m services to fill the 2h window
        booking.services.add(self.service_private)
        booking.services.add(self.service_private)
        
        # Group service needs 60 mins. Overlap is allowed.
        available_dates = get_available_dates([self.service_overlap.id], start_date=target_date)
        self.assertIn(target_date.strftime('%Y-%m-%d'), available_dates)

    def test_mixed_services_strict_wins(self):
        """
        If one service is private, the whole booking follows strict conflict detection.
        """
        target_date = date(2026, 6, 1)
        
        # Book 09:30 to 10:30
        start_time = timezone.make_aware(datetime.combine(target_date, time(9, 30)))
        booking = Booking.objects.create(
            client_name="Test",
            client_email="test@test.com",
            start_time=start_time,
            status="CONFIRMED"
        )
        booking.services.add(self.service_private)
        
        # Request both Private and Group. Total 120m.
        # Strict mode will see the booking and fail.
        available_dates = get_available_dates([self.service_private.id, self.service_overlap.id], start_date=target_date)
        self.assertNotIn(target_date.strftime('%Y-%m-%d'), available_dates)
