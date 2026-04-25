# Design: Service Availability Validation Engine

## Architectural Overview
The `_is_day_available` function will be refactored into a multi-stage pipeline:
1. **Range Validation**: Determine if the date is within an enabled `AvailabilityRange`.
2. **Weekday Validation**: Determine if the weekday is enabled by `AvailabilitySlot`.
3. **Override Processing**: Apply specific date-time overrides (positive or negative).

## Implementation Details
- **Batch Pre-fetching**: For the 30-day window, fetch all relevant `AvailabilityRange`, `AvailabilitySlot`, and `Override` records for both the services and the company profile once.
- **Intersection Logic**: Since we are checking multiple services, we will implement an "intersection" strategy: a day is available only if `True` for all requested services.
- **Fallback Pattern**: For any entity (service/company), if no records of a specific type (range/slot) exist, treat as "always enabled". If records do exist, validate against them.
