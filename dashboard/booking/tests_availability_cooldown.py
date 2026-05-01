from django.test import TestCase
from datetime import date, timedelta, time, datetime
from booking.models import CompanyProfile, EventType, Event, AvailabilitySlot, Booking, CompanyAvailability
from utils.availability import get_available_dates, get_available_slots
from django.utils import timezone

class CooldownTest(TestCase):
    def setUp(self):
        self.profile = CompanyProfile.get_solo()
        self.profile.booking_cooldown_minutes = 15
        self.profile.save()

        self.category = EventType.objects.create(name="Beauty", allow_overlap=False)
        self.service = Event.objects.create(
            event_type=self.category,
            name="Service",
            price="50.00",
            duration_minutes=30
        )
        
        # Company Availability: 09:00 to 12:00
        CompanyAvailability.objects.create(
            company=self.profile,
            start_date=date(2026, 1, 1),
            end_date=date(2026, 12, 31)
        )
        for i in range(7):
            AvailabilitySlot.objects.create(event=self.service, weekday=i, start_time="09:00:00", end_time="12:00:00")

    def test_cooldown_between_bookings(self):
        """
        Verify that cooldown is enforced after a booking.
        """
        target_date = date(2026, 6, 1) # a Monday
        
        # Book 10:00 to 10:30
        start_time = timezone.make_aware(datetime.combine(target_date, time(10, 0)))
        booking = Booking.objects.create(
            client_name="Test",
            client_email="test@test.com",
            start_time=start_time,
            status="CONFIRMED"
        )
        booking.services.add(self.service) # 30 mins
        
        # Available slots should respect 15 min cooldown.
        # Booking ends at 10:30. Next slot should be at 10:45 (10:30 + 15 min).
        # Booking starts at 10:00. Previous slot should end by 09:45 (10:00 - 15 min).
        # Service duration is 30 mins. 
        # Slot at 09:15 ends at 09:45. (OK)
        # Slot at 09:30 ends at 10:00. (CONFLICT with cooldown)
        
        slots = get_available_slots(target_date, [self.service.id])
        
        self.assertIn("09:15", slots)
        self.assertNotIn("09:30", slots)
        self.assertNotIn("09:45", slots)
        self.assertNotIn("10:00", slots)
        self.assertNotIn("10:15", slots)
        self.assertNotIn("10:30", slots)
        self.assertIn("10:45", slots)

    def test_grid_alignment_with_odd_cooldown(self):
        """
        Verify that slots still align to 15-min grid even if cooldown/duration creates odd gaps.
        """
        self.profile.booking_cooldown_minutes = 10
        self.profile.save()
        
        target_date = date(2026, 6, 1)
        
        # Service duration is 30 mins.
        # Book 10:00 to 10:30.
        start_time = timezone.make_aware(datetime.combine(target_date, time(10, 0)))
        booking = Booking.objects.create(
            client_name="Test",
            client_email="test@test.com",
            start_time=start_time,
            status="CONFIRMED"
        )
        booking.services.add(self.service)
        
        # Cooldown is 10 mins.
        # Window ends at 10:30 + 10 = 10:40.
        # Next available time is 10:40, but grid alignment should push it to 10:45.
        
        slots = get_available_slots(target_date, [self.service.id])
        self.assertNotIn("10:40", slots)
        self.assertIn("10:45", slots)

    def test_day_availability_with_cooldown(self):
        """
        Verify that day is marked unavailable if only gap is smaller than duration + cooldown.
        """
        target_date = date(2026, 6, 1)
        
        # Available 09:00 - 12:00 (3 hours = 180 mins)
        # We want to fill it so only a small gap remains.
        # Booking 1: 09:00 - 10:00
        # Booking 2: 10:40 - 12:00
        # Gap: 10:00 - 10:40 (40 mins)
        # Required: 30 mins service + 15 mins cooldown (both sides) = 60 mins gap needed if between?
        # Actually, between B1 and B2, we need: B1.end + 15 <= N.start AND N.end + 15 <= B2.start.
        # So N.start >= 10:15 and N.end <= 10:25.
        # Duration is 30 mins. 10:15 to 10:25 is only 10 mins.
        
        b1_start = timezone.make_aware(datetime.combine(target_date, time(9, 0)))
        booking1 = Booking.objects.create(client_name="T1", client_email="t1@t.com", start_time=b1_start, status="CONFIRMED")
        # Need a service to make it 60 mins
        s60 = Event.objects.create(event_type=self.category, name="S60", price="0", duration_minutes=60)
        booking1.services.add(s60)
        
        b2_start = timezone.make_aware(datetime.combine(target_date, time(10, 40)))
        booking2 = Booking.objects.create(client_name="T2", client_email="t2@t.com", start_time=b2_start, status="CONFIRMED")
        booking2.services.add(s60) # 60 mins, ends at 11:40
        
        available_dates = get_available_dates([self.service.id], start_date=target_date)
        self.assertNotIn(target_date.strftime('%Y-%m-%d'), available_dates)
