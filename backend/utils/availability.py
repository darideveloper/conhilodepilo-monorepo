from datetime import datetime, timedelta
from booking.models import Event, Booking, CompanyAvailability, CompanyWeekdaySlot, CompanyDateOverride, AvailabilitySlot, EventDateOverride, EventAvailability

def get_available_dates(service_ids, start_date=None):
    if start_date is None:
        start_date = datetime.today().date()
    
    end_date = start_date + timedelta(days=30)
    services = Event.objects.filter(id__in=service_ids)
    
    if not services.exists():
        return []

    available_dates = []
    
    # Pre-fetch relevant data
    # In a real system, we'd fetch all relevant overrides/ranges for the 30 days
    
    for i in range(30):
        current_date = start_date + timedelta(days=i)
        if _is_day_available(current_date, services):
            available_dates.append(current_date.strftime('%Y-%m-%d'))
            
    return available_dates

def _is_day_available(day, services):
    for service in services:
        # 1. Availability Ranges
        ranges = service.availabilities.all()
        if ranges.exists():
            if not ranges.filter(start_date__lte=day, end_date__gte=day).exists():
                return False
        else:
            if CompanyAvailability.objects.exists():
                if not CompanyAvailability.objects.filter(start_date__lte=day, end_date__gte=day).exists():
                    return False

        # 2. Overrides (Check first so they take precedence over slot rules)
        service_override = service.overrides.filter(date=day).first()
        company_override = CompanyDateOverride.objects.filter(date=day).first()
        override = service_override or company_override

        if override:
            if not override.is_available:
                return False
            return True # Explicitly available, override takes precedence over slot filtering

        # 3. Weekday Slots
        weekday = day.weekday()
        service_slots = service.slots.filter(weekday=weekday)
        company_slots = CompanyWeekdaySlot.objects.filter(weekday=weekday)
        
        if service.slots.exists():
            if not service_slots.exists():
                return False
        elif CompanyWeekdaySlot.objects.exists():
            if not company_slots.exists():
                return False
            
    return True
