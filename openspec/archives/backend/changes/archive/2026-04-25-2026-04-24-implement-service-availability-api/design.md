# Design: Service Availability API

## Architectural Overview
The availability calculation is a heavy read operation. To maintain performance:
1. **Utility-First Approach**: Logic will be centralized in `utils/availability.py` rather than within the `View` class. This makes the logic unit-testable and reusable.
2. **Batch Querying**: Fetch all bookings, overrides, and slots for the relevant 30-day window in a few optimized DB queries, then perform the calculation in-memory.

## Components
- `utils/availability.py`:
    - `get_available_dates(service_ids, start_date)`: Main entry point.
    - `_check_day(day, services, bookings, ...)`: Internal helper to evaluate if a single day has capacity.
- `booking/views.py`:
    - `AvailabilityView`: Simple API controller that calls the utility and handles serialization.
- `project/urls.py`:
    - Register `/api/availability/days/`.

## Data Model Considerations
- **Overlap Logic**: If `EventType.allow_overlap` is `False`, the cumulative duration of selected services must fit into a single contiguous block within the available hours. If `True`, logic may be simpler.
- **Performance**: 30 days is a small enough window to calculate efficiently in-memory once relevant objects are pre-fetched.
