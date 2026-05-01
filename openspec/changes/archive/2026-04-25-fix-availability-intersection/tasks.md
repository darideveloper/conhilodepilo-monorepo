## 1. Implementation
- [x] 1.1 Update `get_available_dates` in `dashboard/utils/availability.py` to accept and process the `30` day timeframe up-front.
- [x] 1.2 Query all relevant `CompanyAvailability`, `EventAvailability`, `CompanyDateOverride`, `EventDateOverride`, `CompanyWeekdaySlot`, and `AvailabilitySlot` over the window.
- [x] 1.3 Store all of this fetched data within mapped dictionaries keyed by `service.id` and `date` or `weekday` as appropriate.
- [x] 1.4 Modify `_is_day_available` in `dashboard/utils/availability.py` to accept the pre-fetched structured data instead of the `services` QuerySet.
- [x] 1.5 Update the loop logic in `_is_day_available`: Replace `return True` when a positive `DateOverride` is matched with `continue`.
- [x] 1.6 Verify that `get_available_dates` resolves to an accurate date intersection across complex, overlapping scenarios (e.g., standard slot ranges vs overrides).
- [x] 1.7 Verify that the N+1 queries bottleneck is resolved when calling `GET /api/booking/available-days/`.
- [x] 1.8 Update existing tests or write new ones to validate that date intersections calculate correctly and no N+1 database issues exist during availability calculations.
