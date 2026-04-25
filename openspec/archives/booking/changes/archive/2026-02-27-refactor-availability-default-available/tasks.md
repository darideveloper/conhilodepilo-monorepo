# Tasks: Refactor Availability to Default-Available

## Data Migration
- [x] Remove `available` arrays from `src/data/tours.json` for all tours. <!-- id: 0 -->
    - *Validation*: Run `cat src/data/tours.json | grep available` (should return nothing).

## State Management Update
- [x] Refactor `Availability` interface in `src/store/useBookingStore.ts` to remove `available`. <!-- id: 1 -->
- [x] Update `getInitialAvailability` to stop parsing `available` dates. <!-- id: 2 -->
    - *Validation*: Ensure types compile and store initializes correctly.

## UI Logic Refactor
- [x] Update `modifiers` in `BookingCalendar.tsx` to handle default-available logic. <!-- id: 3 -->
- [x] Update `getStatus` helper in `BookingCalendar.tsx` to return 'available' as the default future state. <!-- id: 4 -->
- [x] Update `Calendar` component's `disabled` prop if it specifically relied on the `available` list. <!-- id: 5 -->

## Verification
- [x] Verify that future dates not in `booked` or `limited` are still green in the calendar. <!-- id: 6 -->
- [x] Verify that past dates are still disabled. <!-- id: 7 -->
- [x] Verify that `limited` and `booked` dates still show their respective colors. <!-- id: 8 -->
