# Proposal: Fix Booking Calendar UI Bugs

This proposal addresses two bugs in the `BookingCalendar` component: the selected date color not matching the hover state, and the calendar having a pre-selected value on initial load.

## Why
1.  **Bug 1 (Selected Date Color)**: The selected date should be visually distinct and consistent with the hover state (black background/foreground color). Currently, it uses the primary brand color which can blend with the "available" status color.
2.  **Bug 2 (Initial Selection)**: When the page loads, no date should be selected until the user interacts with the calendar. A pre-selected date can lead to unintended bookings and confuses the user about their choice.

## What Changes
- **BookingCalendar Organism**:
    - Change the initial state of the `date` to `undefined` in `src/components/organisms/BookingCalendar.tsx`.
- **Calendar Atom**:
    - Update the `CalendarDayButton` component in `src/components/atoms/ui/calendar.tsx` to use `bg-foreground` and `text-background` for the single selected state (`data-selected-single=true`).

## Goals
- Improve the visual feedback for the selected date.
- Ensure the booking process starts from a neutral state with no date pre-selected.

## Scope
- `src/components/organisms/BookingCalendar.tsx`
- `src/components/atoms/ui/calendar.tsx`

## Success Criteria
- The selected date in the calendar is rendered with the same style as the hover state (black background).
- The calendar shows no selected date when the page is first loaded.
- All other availability states (booked, limited, available) continue to render correctly.
- `openspec validate` passes.
