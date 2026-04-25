# Tasks: Refine Calendar UI

- [x] **Component UI Cleanup**
    - [x] Remove `CardHeader` and the "Booking Schedule" title/description from `src/components/BookingCalendar.tsx`.

- [x] **Component Styling Refinement**
    - [x] Add a hover style to the calendar days in `src/components/BookingCalendar.tsx` or `src/components/ui/calendar.tsx` to use `brand-charcoal` for background and `white` for text.
    - [x] Ensure consistent brand colors are used for the hover effect across all modifiers.

- [x] **Responsive Page Integration**
    - [x] Update the `index.astro` page to remove the `hidden lg:block` classes on the calendar container.
    - [x] Apply responsive positioning and width classes (e.g., `max-w-md w-full mx-auto lg:fixed lg:top-4 lg:right-4`).

- [x] **Validation**
    - [x] Verify that the calendar is visible on mobile and desktop devices.
    - [x] Verify that the hover state is correctly applied.
    - [x] Confirm the "Booking Schedule" title is removed.
    - [x] Run `openspec validate refine-calendar-ui`.
