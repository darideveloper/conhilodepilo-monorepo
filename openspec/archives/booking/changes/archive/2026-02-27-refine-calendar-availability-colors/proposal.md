# Change: Refine Calendar Availability Colors

## Why
The current calendar color configuration is counter-intuitive. In Granada (and generally), red is associated with "Stop" or "Closed," but the booking system currently uses the brand red (`primary`) for "Available" dates. This leads to user confusion and potentially fewer bookings. This change aligns the calendar's visual language with common mental models (Green = Available, Amber = Limited).

## What Changes
- Update `STATUS_CONFIG` in `src/components/organisms/types.ts` with new intuitive colors for `available` and `limited`.
- Enhance the `modifier` classes for each status to ensure consistent hover and selected states.
- Adjust the `StatusLegend` and `StatusDetails` components (if needed, but they already use `STATUS_CONFIG`) to reflect these changes automatically.

## Impact
- **Affected Specs**: `calendar`.
- **Affected Files**: `src/components/organisms/types.ts`.
- **User Experience**: Improved clarity and trust in the booking flow.
