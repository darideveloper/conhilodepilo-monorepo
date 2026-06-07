from decimal import Decimal
from typing import List, Tuple, Union

def calculate_service_discount(service, quantity: int) -> Tuple[Decimal, int]:
    """
    Calculate discount for a service given a quantity using threshold-style BOGO formula.

    Args:
        service: Event model instance with buy_x and get_y_free fields
        quantity: Number of units being booked

    Returns:
        Tuple of (discount_amount, free_count)
        - discount_amount: Decimal value of total discount
        - free_count: Number of free items awarded
    """
    buy_x = getattr(service, 'buy_x', 0) or 0
    get_y_free = getattr(service, 'get_y_free', 0) or 0

    if buy_x <= 0 or get_y_free <= 0 or quantity <= 0:
        return Decimal('0.00'), 0

    unit_price = getattr(service, 'price', Decimal('0.00')) or Decimal('0.00')

    free_count = min((quantity // buy_x) * get_y_free, quantity)

    discount_amount = Decimal(str(free_count)) * unit_price

    return discount_amount, free_count


def calculate_booking_totals(booking_services: List[Union[tuple, 'BookingServiceThrough']]) -> Tuple[Decimal, Decimal, Decimal, int]:
    """
    Calculate totals for a booking given a list of services with quantities.

    Args:
        booking_services: List of either:
            - tuples of (Event, quantity, unit_price)
            - BookingServiceThrough objects

    Returns:
        Tuple of (original_amount, discount_amount, total_amount, total_duration)
    """
    original_amount = Decimal('0.00')
    discount_amount = Decimal('0.00')
    total_duration = 0

    for bs in booking_services:
        if isinstance(bs, tuple):
            event, quantity, unit_price = bs
        else:
            event = bs.event
            quantity = getattr(bs, 'quantity', 1)
            unit_price = getattr(bs, 'unit_price', getattr(event, 'price', Decimal('0.00')))

        service_total = unit_price * Decimal(str(quantity))
        original_amount += service_total

        discount, _ = calculate_service_discount(event, quantity)
        discount_amount += discount

        duration_minutes = getattr(event, 'duration_minutes', 0) or 0
        total_duration += duration_minutes * quantity

    total_amount = original_amount - discount_amount

    return original_amount, discount_amount, total_amount, total_duration