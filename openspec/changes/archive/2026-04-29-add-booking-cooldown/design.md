# Design: Booking Cooldown Implementation

## Core Logic: The "Double Buffer" Approach
To implement a cooldown `C` between any two reservations, we will treat every existing booking `B` as effectively occupying a "blocked period" of `[B.start - C, B.end + C]`.

### Why this works:
- If a new booking `N` ends at `N.end`, and the next booking `B` starts at `B.start`.
- The blocked period of `B` starts at `B.start - C`.
- The system prevents `N` from overlapping `[B.start - C, B.end + C]`.
- Therefore, `N.end` MUST be `<= B.start - C`.
- This guarantees `B.start - N.end >= C`, exactly fulfilling the requirement.

## Algorithm Updates

### 1. Centralized Window Splitting
We will refactor the logic that subtracts bookings from free windows into a shared utility function. This function will take the `cooldown` as an argument and apply the double-buffer logic.

### 2. Slot Grid Alignment ("Snap to 15")
To prevent the UI from showing "odd" start times (e.g., 12:05), the slot generation will follow these rules:
1. Start at the beginning of a free window `W_start`.
2. Find the first time `T >= W_start` that aligns with the 15-minute grid (00, 15, 30, 45).
3. Generate subsequent slots from `T` using the 15-minute interval.
4. Stop when `T + ServiceDuration > W_end`.

## Implementation Details

### Database
- `CompanyProfile.booking_cooldown_minutes`: Integer field, default 0.

### Validations
- **Date Validation:** `_is_day_available` will use the shrunken free windows to determine if a day can accommodate the requested services.
- **Hour Validation:** `get_available_slots` will use the same shrunken windows to generate valid start times.

## Potential Issues
- **Race Conditions:** `CreateBookingView` performs a "check-then-act" sequence. In high-traffic scenarios, two bookings could still overlap if they are processed simultaneously. A database-level constraint or transaction lock would be required for full atomicity, but is considered out of scope for this specific feature unless requested.
