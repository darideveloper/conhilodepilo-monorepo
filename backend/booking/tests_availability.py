from django.test import TestCase
from datetime import date, timedelta
from booking.models import CompanyProfile, EventType, Event, EventAvailability, EventDateOverride, AvailabilitySlot
from utils.availability import get_available_dates
from django.db import reset_queries

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
        Service A: 01/01 to 10/01 + 15/01 (override)
        Service B: 05/01 to 10/02
        Intersection should be 05/01 to 10/01. 15/01 should NOT be included.
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
        
        # We expect a constant number of queries regardless of the 30-day loop.
        # 1. Event.objects.filter(id__in=service_ids)
        # 2. EventAvailability.objects.filter(...)
        # 3. CompanyAvailability.objects.filter(...)
        # 4. EventDateOverride.objects.filter(...)
        # 5. CompanyDateOverride.objects.filter(...)
        # 6. AvailabilitySlot.objects.filter(...)
        # 7. AvailabilitySlot.objects.filter(...).values_list('event_id', flat=True).distinct()
        # 8. CompanyWeekdaySlot.objects.all()
        # 9. CompanyWeekdaySlot.objects.exists()
        
        # Let's count them exactly.
        with self.assertNumQueries(9):
            get_available_dates(service_ids, start_date=date(2026, 1, 1))
