# Design: Booking Calendar UI Refinement

## Architectural Reasoning
The refinements focus on **Composition** and **Responsive Design**. By removing unnecessary headers and adjusting visibility classes, we create a more focused and accessible "island" of interactivity.

### Brand Color Hover
We will use the existing `brand-charcoal` (oklch(0.141 0.005 285.823)) for the hover state of the calendar days. This provides a high-contrast, premium feel consistent with the brand's sophisticated aesthetic.

### Responsive Strategy
The current implementation in `index.astro` uses `hidden lg:block`, which explicitly hides the calendar on anything smaller than a desktop. We will change this to a flexible positioning strategy:
- **Mobile**: Centered or inline with max width.
- **Desktop**: Fixed positioning as originally intended.

## Implementation Details

### src/components/BookingCalendar.tsx
- Remove `CardHeader` and its children.
- Add or modify the calendar's day cell styles to include `hover:bg-brand-charcoal hover:text-white`.
*Note: Since the calendar is a shadcn component, we might need to update `src/components/ui/calendar.tsx` or pass specific `classNames` to the `Calendar` component in `BookingCalendar.tsx`.*

### src/pages/index.astro
- Change `fixed top-4 right-4 z-50 max-w-sm hidden lg:block` to classes that allow for mobile visibility. 
- Suggestion: `lg:fixed lg:top-4 lg:right-4 z-50 w-full lg:max-w-sm p-4 lg:p-0`.

## Trade-offs
- **Mobile Real Estate**: A calendar can take up significant vertical space on mobile. We will ensure it uses `max-width` and potentially adjust its positioning so it doesn't overlap critical content if used as `fixed`. 
- **Global vs Local Styling**: We will prefer passing `classNames` to the calendar to keep the change scoped to the `BookingCalendar` integration unless a global change to all calendars is desired.
