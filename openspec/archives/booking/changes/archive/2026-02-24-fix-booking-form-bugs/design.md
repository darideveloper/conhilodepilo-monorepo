# Design: Booking Calendar UI Fixes

## Architectural Reasoning
The fixes are centered around improving the user interaction with the `BookingCalendar` organism and the `Calendar` atom.

### Selected State Color Consistency
The `CalendarDayButton` currently uses `data-[selected-single=true]:bg-primary`, which overlaps with the `available` modifier's color. By using `bg-foreground` (which represents the dark/black charcoal brand color) and `text-background` (cream/white), the selected date will stand out clearly and align with the existing hover pattern.

### Initial Selection Neutrality
The `BookingCalendar` state was initialized to `today`. While this may seem helpful, it can lead to confusion if the user doesn't realize a date is pre-selected. Changing the initial state to `undefined` ensures that the user must explicitly choose a date to proceed.

## Implementation Details

### src/components/organisms/BookingCalendar.tsx
- Change `useState<Date | undefined>(today)` to `useState<Date | undefined>(undefined)`.

### src/components/atoms/ui/calendar.tsx
- In `CalendarDayButton`, change `data-[selected-single=true]:bg-primary` to `data-[selected-single=true]:bg-foreground`.
- In `CalendarDayButton`, change `data-[selected-single=true]:text-primary-foreground` to `data-[selected-single=true]:text-background`.

## Trade-offs
- **User Convenience**: Pre-selecting "today" can be convenient if most bookings are for today, but for tours in Granada, users typically plan in advance. A neutral starting point is safer and more professional.
- **Component Reusability**: The change in `CalendarDayButton` affects all instances of the `Calendar` component. Since the brand identity uses these colors consistently, this is an acceptable and desired global change.
