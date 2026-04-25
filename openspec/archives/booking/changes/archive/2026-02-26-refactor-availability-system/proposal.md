# Refactor Availability System

## Why
Currently, the `BookingCalendar` component uses hardcoded dates for `available`, `limited`, and `booked` statuses. This makes it impossible to manage availability on a per-tour basis or update it without changing the code.

## What Changes
1.  **Update Data Model**: Add a `dates` object to each tour in `src/data/tours.json` containing `available`, `limited`, and `booked` arrays of ISO date strings (YYYY-MM-DD).
2.  **State Management**: Update `useBookingStore.ts` to expose the current availability dates based on the selected tour.
3.  **Dynamic UI**: Refactor `BookingCalendar` to consume the availability data from the store instead of hardcoded constants.
4.  **Automatic Updates**: Ensure that selecting a tour in `BookingForm` triggers an update of the availability in the calendar.

## Impact
- **Tours Data**: Each tour will now define its own weekly availability.
- **Booking Store**: Will act as the single source of truth for tour-specific availability.
- **Calendar UI**: Will accurately reflect the availability of the selected tour.
