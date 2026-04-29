# Change: Add Booking Cooldown

## Why
Currently, the system allows bookings to be scheduled back-to-back without any buffer time. This is impractical for many businesses that need time for cleanup, preparation, or transition between clients. Implementing a manageable "cool down" period ensures that the schedule is realistic and sustainable.

## What Changes
- **Backend Models:** Add `booking_cooldown_minutes` to the `CompanyProfile` model (managed via Django Admin).
- **Availability Logic:** Update the availability engine to treat every existing booking as having a "buffer zone" before and after its scheduled time.
- **Refactoring:** Centralize the free-window calculation to ensure consistent cooldown enforcement across both day-level availability and slot-level generation.
- **Grid Consistency:** Ensure that even with dynamic cooldowns, the system continues to suggest start times that align with the business's 15-minute scheduling grid.

## Impact
- **Affected Specs:** `availability-logic`, `backend-models`.
- **Affected Code:** `backend/booking/models.py`, `backend/booking/serializers.py`, `backend/utils/availability.py`.
- **UX Impact:** Users will see fewer available slots, but the slots shown will be guaranteed to have the required buffer time relative to existing appointments.
