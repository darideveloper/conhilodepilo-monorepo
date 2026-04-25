from datetime import datetime, timedelta
from collections import defaultdict
from booking.models import Event, Booking, CompanyAvailability, CompanyWeekdaySlot, CompanyDateOverride, AvailabilitySlot, EventDateOverride, EventAvailability

def get_available_dates(service_ids, start_date=None):
    if start_date is None:
        start_date = datetime.today().date()
    
    end_date = start_date + timedelta(days=29)
    services = Event.objects.filter(id__in=service_ids)
    
    if not services.exists():
        return []

    # 1. Fetch Availability Ranges
    s_avail = defaultdict(list)
    for a in EventAvailability.objects.filter(event_id__in=service_ids, start_date__lte=end_date, end_date__gte=start_date):
        s_avail[a.event_id].append(a)
    
    c_avail = list(CompanyAvailability.objects.filter(start_date__lte=end_date, end_date__gte=start_date))

    # 2. Fetch Overrides
    s_overrides = {} # (event_id, date) -> override
    for o in EventDateOverride.objects.filter(event_id__in=service_ids, date__gte=start_date, date__lte=end_date):
        s_overrides[(o.event_id, o.date)] = o
    
    c_overrides = {o.date: o for o in CompanyDateOverride.objects.filter(date__gte=start_date, date__lte=end_date)}

    # 3. Fetch Weekday Slots
    s_slots = defaultdict(lambda: defaultdict(list))
    for s in AvailabilitySlot.objects.filter(event_id__in=service_ids):
        s_slots[s.event_id][s.weekday].append(s)
    
    services_with_any_slots = set(AvailabilitySlot.objects.filter(event_id__in=service_ids).values_list('event_id', flat=True).distinct())

    c_slots = defaultdict(list)
    for s in CompanyWeekdaySlot.objects.all():
        c_slots[s.weekday].append(s)
    
    has_c_slots = CompanyWeekdaySlot.objects.exists()

    context = {
        'service_availabilities': s_avail,
        'company_availabilities': c_avail,
        'service_overrides': s_overrides,
        'company_overrides': c_overrides,
        'service_slots': s_slots,
        'services_with_any_slots': services_with_any_slots,
        'company_slots': c_slots,
        'has_company_slots': has_c_slots,
        'service_ids': service_ids
    }

    available_dates = []
    for i in range(30):
        current_date = start_date + timedelta(days=i)
        if _is_day_available(current_date, context):
            available_dates.append(current_date.strftime('%Y-%m-%d'))
            
    return available_dates

def _is_day_available(day, context):
    for s_id in context['service_ids']:
        # 1. Availability Ranges
        s_ranges = context['service_availabilities'].get(s_id, [])
        if s_ranges:
            if not any(r.start_date <= day <= r.end_date for r in s_ranges):
                return False
        else:
            if context['company_availabilities']:
                if not any(r.start_date <= day <= r.end_date for r in context['company_availabilities']):
                    return False

        # 2. Overrides
        s_override = context['service_overrides'].get((s_id, day))
        c_override = context['company_overrides'].get(day)
        override = s_override or c_override

        if override:
            if not override.is_available:
                return False
            continue # Corrected logic: skip to next service

        # 3. Weekday Slots
        weekday = day.weekday()
        if s_id in context['services_with_any_slots']:
            if not context['service_slots'][s_id].get(weekday):
                return False
        elif context['has_company_slots']:
            if not context['company_slots'].get(weekday):
                return False
            
    return True
