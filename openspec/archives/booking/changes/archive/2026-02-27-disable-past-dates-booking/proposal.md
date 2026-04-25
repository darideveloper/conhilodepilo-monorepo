# Change: Disable Past Dates in Booking Calendar

## Why
Currently, the booking calendar allows users to see availability and potentially select dates that have already passed or the current day. To ensure a professional and realistic booking experience, users should only be able to book tours starting from tomorrow.

## What Changes
- Implement a `today` reference in `BookingCalendar.tsx`.
- Disable all dates on or before `today` in the `Calendar` component.
- Ensure availability modifiers (green for Available, gold for Limited) are not applied to past or current dates.
- Update `getStatus` logic to treat past/current dates as 'standard' (neutral) to avoid confusing status details.

## Impact
- Affected spec: `calendar`.
- Affected code: `src/components/organisms/BookingCalendar.tsx`.
