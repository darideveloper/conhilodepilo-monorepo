# Proposal: Apply Virtual Limited Availability

## Problem
Currently, the "Limited" availability status depends entirely on the `src/data/tours.json` file. The business requirement is that the next 10 days from today should **always** be marked as "Limited" for any selected tour, unless they are explicitly marked as "Booked". This should be calculated dynamically without modifying the source JSON.

## Proposed Solution
Inject "Virtual Limited" dates into the booking system's logic.
1.  In `src/store/useBookingStore.ts`, modify `getInitialAvailability` to calculate the next 10 days from the current date.
2.  Add any future date within that 10-day window to the `limited` array if it isn't already in the `booked` array.
3.  This ensures that both the `BookingCalendar` modifiers and the `StatusDetails` component (which uses `getStatus`) reflect this real-time logic.

## Impact
- **Consistency**: All tours will show the next 10 days as limited.
- **Real-time**: The calculation happens on tour selection/load, ensuring "next 10 days" is always relative to the user's current time.
- **Maintainability**: No need to manually update `tours.json` for rolling "limited" windows.
