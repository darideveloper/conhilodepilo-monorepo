from datetime import datetime, timedelta, time
from collections import defaultdict
from django.utils import timezone
from booking.models import Event, Booking, CompanyAvailability, CompanyWeekdaySlot, CompanyDateOverride, AvailabilitySlot, EventDateOverride, EventAvailability, CompanyProfile

def get_available_dates(service_ids, start_date=None):
    if start_date is None:
        start_date = timezone.now().date()
    
    end_date = start_date + timedelta(days=29)
    # Prefetch event_type to get allow_overlap flag
    services = list(Event.objects.filter(id__in=service_ids).select_related('event_type'))
    
    if not services:
        return []

    total_duration = sum(s.duration_minutes for s in services)
    all_allow_overlap = all(s.event_type.allow_overlap for s in services)
    company_profile = CompanyProfile.get_solo()
    cooldown = company_profile.booking_cooldown_minutes

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

    # 4. Fetch Bookings (O(1) query)
    # We fetch bookings that might affect our 30-day window
    start_dt = timezone.make_aware(datetime.combine(start_date, time.min))
    end_dt = timezone.make_aware(datetime.combine(end_date, time.max))
    
    bookings = Booking.objects.filter(
        start_time__lt=end_dt,
        end_time__gt=start_dt
    ).exclude(status="CANCELLED")

    bookings_by_date = defaultdict(list)
    for b in bookings:
        # Using .date() of start_time is usually enough for daily checks
        bookings_by_date[b.start_time.date()].append(b)

    context = {
        'service_availabilities': s_avail,
        'company_availabilities': c_avail,
        'service_overrides': s_overrides,
        'company_overrides': c_overrides,
        'service_slots': s_slots,
        'services_with_any_slots': services_with_any_slots,
        'company_slots': c_slots,
        'has_company_slots': has_c_slots,
        'service_ids': service_ids,
        'total_duration': total_duration,
        'all_allow_overlap': all_allow_overlap,
        'bookings_by_date': bookings_by_date,
        'cooldown': cooldown
    }

    available_dates = []
    for i in range(30):
        current_date = start_date + timedelta(days=i)
        if _is_day_available(current_date, context):
            available_dates.append(current_date.strftime('%Y-%m-%d'))
            
    return available_dates

def _is_day_available(day, context):
    # 1. Check basic constraints for each service
    for s_id in context['service_ids']:
        # Availability Ranges
        s_ranges = context['service_availabilities'].get(s_id, [])
        if s_ranges:
            if not any(r.start_date <= day <= r.end_date for r in s_ranges):
                return False
        else:
            if context['company_availabilities']:
                if not any(r.start_date <= day <= r.end_date for r in context['company_availabilities']):
                    return False

        # Overrides & Weekday Presence
        s_override = context['service_overrides'].get((s_id, day))
        c_override = context['company_overrides'].get(day)
        
        # If any is specifically unavailable, the day is out
        if (s_override and not s_override.is_available) or (c_override and not c_override.is_available):
            return False
            
        # Check weekday slot existence (only if not overridden as available)
        if not (s_override and s_override.is_available) and not (c_override and c_override.is_available):
            weekday = day.weekday()
            if s_id in context['services_with_any_slots']:
                if not context['service_slots'][s_id].get(weekday):
                    return False
            elif context['has_company_slots']:
                if not context['company_slots'].get(weekday):
                    return False
    
    # 2. Check for at least one free window of sufficient duration
    # We need to find the "Working Windows" for the day and subtract bookings (if no overlap)
    working_windows = _get_combined_windows(day, context)
    if not working_windows:
        return False
        
    if context['all_allow_overlap']:
        # If overlap is allowed, we just need to fit in business hours
        return any((w[1].hour * 60 + w[1].minute) - (w[0].hour * 60 + w[0].minute) >= context['total_duration'] for w in working_windows)
    
    # Subtract bookings
    bookings = context['bookings_by_date'].get(day, [])
    free_windows = _get_free_windows(working_windows, bookings, context['cooldown'])
        
    # Check if any free window is large enough
    for w_start, w_end in free_windows:
        duration = (w_end.hour * 60 + w_end.minute) - (w_start.hour * 60 + w_start.minute)
        if duration >= context['total_duration']:
            return True
            
    return False

def get_available_slots(day, service_ids):
    """
    Returns a list of available HH:MM start times for a specific date and services.
    """
    # 1. Fetch data for this day
    services = list(Event.objects.filter(id__in=service_ids).select_related('event_type'))
    if not services:
        return []

    total_duration = sum(s.duration_minutes for s in services)
    all_allow_overlap = all(s.event_type.allow_overlap for s in services)

    # Build a minimal context for this day
    s_avail = defaultdict(list)
    for a in EventAvailability.objects.filter(event_id__in=service_ids, start_date__lte=day, end_date__gte=day):
        s_avail[a.event_id].append(a)
    c_avail = list(CompanyAvailability.objects.filter(start_date__lte=day, end_date__gte=day))

    s_overrides = {(o.event_id, o.date): o for o in EventDateOverride.objects.filter(event_id__in=service_ids, date=day)}
    c_overrides = {o.date: o for o in CompanyDateOverride.objects.filter(date=day)}

    s_slots = defaultdict(lambda: defaultdict(list))
    for s in AvailabilitySlot.objects.filter(event_id__in=service_ids):
        s_slots[s.event_id][s.weekday].append(s)
    
    services_with_any_slots = set(AvailabilitySlot.objects.filter(event_id__in=service_ids).values_list('event_id', flat=True).distinct())

    c_slots = defaultdict(list)
    for s in CompanyWeekdaySlot.objects.all():
        c_slots[s.weekday].append(s)
    
    has_c_slots = CompanyWeekdaySlot.objects.exists()

    start_dt = timezone.make_aware(datetime.combine(day, time.min))
    end_dt = timezone.make_aware(datetime.combine(day, time.max))
    bookings = Booking.objects.filter(
        start_time__lt=end_dt,
        end_time__gt=start_dt
    ).exclude(status="CANCELLED")

    # Grouping is simple since it's one day
    bookings_list = list(bookings)
    company_profile = CompanyProfile.get_solo()
    cooldown = company_profile.booking_cooldown_minutes

    context = {
        'service_availabilities': s_avail,
        'company_availabilities': c_avail,
        'service_overrides': s_overrides,
        'company_overrides': c_overrides,
        'service_slots': s_slots,
        'services_with_any_slots': services_with_any_slots,
        'company_slots': c_slots,
        'has_company_slots': has_c_slots,
        'service_ids': service_ids,
        'total_duration': total_duration,
        'all_allow_overlap': all_allow_overlap,
        'cooldown': cooldown
    }

    # 2. Get combined working windows
    working_windows = _get_combined_windows(day, context)
    if not working_windows:
        return []

    # 3. Calculate free windows
    free_windows = working_windows
    if not all_allow_overlap:
        free_windows = _get_free_windows(working_windows, bookings_list, context['cooldown'])

    # 4. Generate slots (15-min interval)
    slots = []
    interval = 15
    now_local = timezone.localtime(timezone.now())
    
    for w_start, w_end in free_windows:
        # Snap w_start to the next 15-minute grid
        start_dt = timezone.make_aware(datetime.combine(day, w_start))
        minutes_to_add = (interval - (start_dt.minute % interval)) % interval
        curr_dt = start_dt + timedelta(minutes=minutes_to_add)
        
        end_dt_limit = timezone.make_aware(datetime.combine(day, w_end))
        
        while curr_dt + timedelta(minutes=total_duration) <= end_dt_limit:
            if curr_dt >= now_local:
                slots.append(curr_dt.time().strftime('%H:%M'))
            curr_dt += timedelta(minutes=interval)
            
    return slots

def _get_free_windows(working_windows, bookings, cooldown):
    """
    Subtracts bookings from working windows, accounting for cooldown.
    """
    free_windows = working_windows
    
    for b in bookings:
        new_free_windows = []
        b_local_start = timezone.localtime(b.start_time)
        b_local_end = timezone.localtime(b.end_time)
        
        # Apply cooldown to the booking boundaries
        # b_start_dt = b_local_start - cooldown
        # b_end_dt = b_local_end + cooldown
        
        b_start_dt = b_local_start - timedelta(minutes=cooldown)
        b_end_dt = b_local_end + timedelta(minutes=cooldown)
        
        # We only care about the time part for window splitting within a day
        if b_start_dt.date() < b_local_start.date():
            b_start = time.min
        else:
            b_start = b_start_dt.time()
            
        if b_end_dt.date() > b_local_end.date():
            b_end = time.max
        else:
            b_end = b_end_dt.time()

        for w_start, w_end in free_windows:
            if b_end <= w_start or b_start >= w_end:
                new_free_windows.append((w_start, w_end))
            else:
                if b_start > w_start:
                    new_free_windows.append((w_start, b_start))
                if b_end < w_end:
                    new_free_windows.append((b_end, w_end))
        free_windows = new_free_windows
        
    return free_windows

def _get_combined_windows(day, context):
    """
    Returns a list of (start_time, end_time) representing the intersection of 
    availability for all selected services on a given day.
    """
    weekday = day.weekday()
    combined_windows = None # Start with None to indicate "all day" for intersection
    
    for s_id in context['service_ids']:
        service_windows = []
        s_override = context['service_overrides'].get((s_id, day))
        if s_override and s_override.is_available:
            service_windows.append((s_override.start_time, s_override.end_time))
        elif s_id in context['services_with_any_slots']:
            for slot in context['service_slots'][s_id][weekday]:
                service_windows.append((slot.start_time, slot.end_time))
        else:
            # Fallback to company
            c_override = context['company_overrides'].get(day)
            if c_override and c_override.is_available:
                service_windows.append((c_override.start_time, c_override.end_time))
            elif context['has_company_slots']:
                for slot in context['company_slots'][weekday]:
                    service_windows.append((slot.start_time, slot.end_time))
        
        if not service_windows:
            return [] # One service has no availability
            
        if combined_windows is None:
            combined_windows = service_windows
        else:
            # Intersect combined_windows with service_windows
            new_combined = []
            for cw_start, cw_end in combined_windows:
                for sw_start, sw_end in service_windows:
                    intersect_start = max(cw_start, sw_start)
                    intersect_end = min(cw_end, sw_end)
                    if intersect_start < intersect_end:
                        new_combined.append((intersect_start, intersect_end))
            combined_windows = new_combined
            if not combined_windows:
                return []
                
    return combined_windows
