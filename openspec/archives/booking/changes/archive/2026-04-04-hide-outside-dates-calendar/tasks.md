# Tasks: Hide Outside Dates in Booking Calendar

- [x] **Implementation: Configure Calendar Prop**
  - Update `src/components/organisms/BookingCalendar.tsx` to set `showOutsideDays={false}` on the `<Calendar />` component.
  - Verification: Open the booking flow, navigate to a month that would typically show outside days (e.g., May 2026), and confirm those days are no longer visible or selectable.
- [x] **Specification: Update Calendar Spec**
  - Add the `Requirement: Show Current Month Dates Only` to the `calendar` specification delta.
  - Verification: Run `openspec validate hide-outside-dates-calendar --strict`.
