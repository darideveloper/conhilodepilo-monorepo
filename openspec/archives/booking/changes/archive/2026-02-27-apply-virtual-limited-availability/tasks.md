# Tasks: Apply Virtual Limited Availability

## State Management
- [x] Add `injectVirtualLimitedDates` helper to `src/store/useBookingStore.ts`. <!-- id: 0 -->
- [x] Integrate the helper into `getInitialAvailability` to supplement the `limited` dates array. <!-- id: 1 -->

## Verification
- [x] Verify next 10 days are amber in the calendar. <!-- id: 2 -->
- [x] Verify booked dates within next 10 days remain slate. <!-- id: 3 -->
- [x] Verify status card shows "Limitada" for these dates. <!-- id: 4 -->
