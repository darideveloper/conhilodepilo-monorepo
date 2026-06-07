from decimal import Decimal
from typing import List, Tuple, Union

def calculate_service_discount(unit_price: Decimal, quantity: int, buy_x: int, get_y_free: int) -> Tuple[Decimal, int]:
    """
    Calculate discount for a service given a quantity using threshold-style BOGO formula.

    Args:
        unit_price: Price per unit
        quantity: Number of units being booked
        buy_x: Number of units to trigger promotion
        get_y_free: Number of free units per threshold

    Returns:
        Tuple of (discount_amount, free_count)
        - discount_amount: Decimal value of total discount
        - free_count: Number of free items awarded
    """
    if buy_x <= 0 or get_y_free <= 0 or quantity <= 0:
        return Decimal('0.00'), 0

    free_count = min((quantity // buy_x) * get_y_free, quantity)

    discount_amount = Decimal(str(free_count)) * unit_price

    return discount_amount, free_count


def calculate_booking_totals(booking_services: List[Union[tuple, 'BookingServiceThrough']], buy_x: int = None, get_y_free: int = None) -> Tuple[Decimal, Decimal, Decimal, int]:
    """
    Calculate totals for a booking given a list of services with quantities.

    Args:
        booking_services: List of either:
            - tuples of (Event, quantity, unit_price)
            - BookingServiceThrough objects
        buy_x: Global BOGO threshold (optional, reads from CompanyProfile if None)
        get_y_free: Global BOGO free count (optional, reads from CompanyProfile if None)

    Returns:
        Tuple of (original_amount, discount_amount, total_amount, total_duration)
    """
    if buy_x is None or get_y_free is None:
        from booking.models import CompanyProfile
        cp = CompanyProfile.get_solo()
        if buy_x is None:
            buy_x = cp.buy_x
        if get_y_free is None:
            get_y_free = cp.get_y_free

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

        discount, _ = calculate_service_discount(unit_price, quantity, buy_x, get_y_free)
        discount_amount += discount

        duration_minutes = getattr(event, 'duration_minutes', 0) or 0
        total_duration += duration_minutes * quantity

    total_amount = original_amount - discount_amount

    return original_amount, discount_amount, total_amount, total_duration