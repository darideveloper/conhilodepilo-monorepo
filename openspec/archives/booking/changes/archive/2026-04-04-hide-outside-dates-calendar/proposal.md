# Proposal: Hide Outside Dates in Booking Calendar

## Summary
The `BookingCalendar` currently displays and allows the selection of dates from adjacent months (e.g., seeing and selecting April 30th when viewing May). This behavior can lead to user confusion during the booking process. This proposal aims to hide these "outside days" by configuring the `Calendar` component to only show dates for the currently selected month.

## Problem
When a user navigates through the calendar, the standard behavior of `react-day-picker` (via our `Calendar` atom) is to show "outside days" to complete the calendar grid. These days are interactive by default, which is not ideal for a booking flow where the month's context is important.

## Proposed Solution
Modify `src/components/organisms/BookingCalendar.tsx` to pass the `showOutsideDays={false}` prop to the `<Calendar />` component. This will hide any dates that do not belong to the month being displayed.

## Scope
- `src/components/organisms/BookingCalendar.tsx`: Update the `<Calendar />` component usage.
- `openspec/specs/calendar/spec.md`: Add a requirement to ensure outside days are hidden.
