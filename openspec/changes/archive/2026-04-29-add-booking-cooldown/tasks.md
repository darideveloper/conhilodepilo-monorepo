## 1. Backend: Data Model & API
- [x] 1.1 Add `booking_cooldown_minutes` field to `CompanyProfile` model in `backend/booking/models.py` (Default: 0).
- [x] 1.2 Create and apply database migration for the new field.
- [x] 1.3 Add `booking_cooldown_minutes` to `CompanyProfileSerializer` in `backend/booking/serializers.py`.

## 2. Backend: Availability Logic Refactor & Update
- [x] 2.1 Refactor window-splitting logic in `backend/utils/availability.py` into a helper function `_get_free_windows(working_windows, bookings, cooldown)`.
- [x] 2.2 Implement "Double Buffer" logic (buffer existing bookings by `C` on both sides) in the helper.
- [x] 2.3 Update `_is_day_available` to use the new helper.
- [x] 2.4 Update `get_available_slots` to use the new helper.
- [x] 2.5 Refine `get_available_slots` to ensure start times align with the 15-minute grid after accounting for cooldown.

## 3. Frontend: Store & Config
- [x] 3.1 Update `AppConfig` interface in `booking/src/store/useBookingStore.ts` to include `booking_cooldown_minutes`.

## 4. Verification & Testing
- [x] 4.1 Create tests in `backend/booking/tests_availability.py` for:
    - [x] Cooldown enforcement between two bookings.
    - [x] Grid alignment (snap to 15-min) after a booking with an "odd" end time.
    - [x] Day availability correctly reflecting the extra time needed for cooldown.
- [x] 4.2 Manually verify that the Admin panel allows changing the cooldown and it reflects immediately in the frontend calendar.
