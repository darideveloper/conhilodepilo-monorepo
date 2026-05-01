from django.test import TestCase
from django.utils import timezone
from datetime import timedelta, time, date
from django.db import transaction
from django.db.utils import IntegrityError
from .models import CompanyProfile, EventType, Event, Booking, CompanyWeekdaySlot

class EventTypeTest(TestCase):
    def test_image_is_optional(self):
        # Should be able to create without an image
        event_type = EventType.objects.create(name="No Image Type")
        self.assertFalse(bool(event_type.image))

class CompanyProfileTest(TestCase):
    def test_singleton(self):
        CompanyProfile.objects.create(brand_color="#123456")
        
        # Subsequent creates should fail due to id=1 being fixed in SingletonModel
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                CompanyProfile.objects.create(brand_color="#654321")
        
        self.assertEqual(CompanyProfile.objects.count(), 1)

class BookingDurationTest(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(name="Test Type")
        self.event1 = Event.objects.create(
            event_type=self.event_type,
            name="Service A",
            price=10,
            duration_minutes=20
        )
        self.event2 = Event.objects.create(
            event_type=self.event_type,
            name="Service B",
            price=20,
            duration_minutes=40
        )
    
    def test_duration_calculation(self):
        start_time = timezone.now().replace(microsecond=0)
        booking = Booking.objects.create(
            client_name="Test Client",
            client_email="test@example.com",
            start_time=start_time
        )
        booking.services.add(self.event1, self.event2)
        
        # end_time should be start_time + 60 minutes
        expected_end_time = start_time + timedelta(minutes=60)
        
        # Refresh from DB to ensure signal ran and saved
        booking.refresh_from_db()
        self.assertEqual(booking.end_time, expected_end_time)

class AvailabilityConstraintTest(TestCase):
    def setUp(self):
        # Required because CompanyWeekdaySlot has default=1 for company FK
        CompanyProfile.objects.get_or_create(id=1)

    def test_unique_slot(self):
        CompanyWeekdaySlot.objects.create(
            weekday=0,
            start_time=time(9, 0),
            end_time=time(10, 0)
        )
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                CompanyWeekdaySlot.objects.create(
                    weekday=0,
                    start_time=time(9, 0),
                    end_time=time(10, 0)
                )
