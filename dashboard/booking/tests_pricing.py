from decimal import Decimal
from django.test import TestCase
from .models import EventType, Event
from utils.pricing import calculate_service_discount, calculate_booking_totals


class CalculateServiceDiscountTest(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(name="Test Type")

    def test_no_promotion_buy_x_zero(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="No Promo Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=0,
            get_y_free=0
        )
        discount, free_count = calculate_service_discount(event, 3)
        self.assertEqual(discount, Decimal('0.00'))
        self.assertEqual(free_count, 0)

    def test_no_promotion_get_y_zero(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="No Promo Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=0
        )
        discount, free_count = calculate_service_discount(event, 3)
        self.assertEqual(discount, Decimal('0.00'))
        self.assertEqual(free_count, 0)

    def test_qty_below_threshold(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="BOGO Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=1
        )
        discount, free_count = calculate_service_discount(event, 1)
        self.assertEqual(discount, Decimal('0.00'))
        self.assertEqual(free_count, 0)

    def test_qty_at_threshold_buy_2_get_1(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="BOGO Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=1
        )
        discount, free_count = calculate_service_discount(event, 2)
        self.assertEqual(discount, Decimal('30.00'))
        self.assertEqual(free_count, 1)

    def test_qty_above_threshold_buy_2_get_1(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="BOGO Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=1
        )
        discount, free_count = calculate_service_discount(event, 3)
        self.assertEqual(discount, Decimal('30.00'))
        self.assertEqual(free_count, 1)

    def test_qty_4_above_threshold_buy_2_get_1(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="BOGO Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=1
        )
        discount, free_count = calculate_service_discount(event, 4)
        self.assertEqual(discount, Decimal('60.00'))
        self.assertEqual(free_count, 2)

    def test_stacking_buy_3_get_1(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="BOGO Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=3,
            get_y_free=1
        )
        discount, free_count = calculate_service_discount(event, 6)
        self.assertEqual(discount, Decimal('60.00'))
        self.assertEqual(free_count, 2)

    def test_qty_zero(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="BOGO Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=1
        )
        discount, free_count = calculate_service_discount(event, 0)
        self.assertEqual(discount, Decimal('0.00'))
        self.assertEqual(free_count, 0)

    def test_get_y_free_greater_than_buy_x(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="Aggressive Promo",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=1,
            get_y_free=10
        )
        discount, free_count = calculate_service_discount(event, 5)
        self.assertEqual(discount, Decimal('150.00'))
        self.assertEqual(free_count, 5)

    def test_capped_at_qty(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="BOGO Service",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=5
        )
        discount, free_count = calculate_service_discount(event, 3)
        self.assertEqual(free_count, 3)
        self.assertEqual(discount, Decimal('90.00'))

    def test_different_price(self):
        event = Event.objects.create(
            event_type=self.event_type,
            name="Expensive Service",
            price=Decimal('50.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=1
        )
        discount, free_count = calculate_service_discount(event, 2)
        self.assertEqual(discount, Decimal('50.00'))
        self.assertEqual(free_count, 1)


class CalculateBookingTotalsTest(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(name="Test Type")
        self.event1 = Event.objects.create(
            event_type=self.event_type,
            name="Service A",
            price=Decimal('30.00'),
            duration_minutes=30,
            buy_x=2,
            get_y_free=1
        )
        self.event2 = Event.objects.create(
            event_type=self.event_type,
            name="Service B",
            price=Decimal('50.00'),
            duration_minutes=60,
            buy_x=0,
            get_y_free=0
        )

    def test_booking_with_discount(self):
        booking_services = [
            (self.event1, 3, Decimal('30.00'))
        ]
        original, discount, total, duration = calculate_booking_totals(booking_services)
        self.assertEqual(original, Decimal('90.00'))
        self.assertEqual(discount, Decimal('30.00'))
        self.assertEqual(total, Decimal('60.00'))
        self.assertEqual(duration, 90)

    def test_booking_without_discount(self):
        booking_services = [
            (self.event2, 2, Decimal('50.00'))
        ]
        original, discount, total, duration = calculate_booking_totals(booking_services)
        self.assertEqual(original, Decimal('100.00'))
        self.assertEqual(discount, Decimal('0.00'))
        self.assertEqual(total, Decimal('100.00'))
        self.assertEqual(duration, 120)

    def test_mixed_services(self):
        booking_services = [
            (self.event1, 3, Decimal('30.00')),
            (self.event2, 1, Decimal('50.00'))
        ]
        original, discount, total, duration = calculate_booking_totals(booking_services)
        self.assertEqual(original, Decimal('140.00'))
        self.assertEqual(discount, Decimal('30.00'))
        self.assertEqual(total, Decimal('110.00'))
        self.assertEqual(duration, 150)

    def test_empty_services(self):
        booking_services = []
        original, discount, total, duration = calculate_booking_totals(booking_services)
        self.assertEqual(original, Decimal('0.00'))
        self.assertEqual(discount, Decimal('0.00'))
        self.assertEqual(total, Decimal('0.00'))
        self.assertEqual(duration, 0)