# Design: Refine Calendar Availability Colors

## Overview
The current calendar implementation uses the brand's primary red for "Available" dates, which confuses users. The goal is to move to a more intuitive color palette (Green/Amber/Gray) while maintaining consistency with the overall brand aesthetic and ensuring clear hover effects.

## Color Mapping Strategy

| Status | Current Color | New Color (Tailwind) | Reason |
| --- | --- | --- | --- |
| **Available** | `primary` (Red) | `emerald-600` / `emerald-500` | Universal "Go" color, distinct from brand red. |
| **Limited** | `muted` (Gray) | `amber-500` / `amber-400` | Warning color, creates urgency for "last spots." |
| **Booked** | `destructive` (Red) | `slate-200` / `slate-100` | Neutral/Disabled feel, with strike-through. |
| **Standard** | `accent` (Beige) | `background` | Neutral default state. |

## Hover State Consistency
The `react-day-picker` (via `shadcn/ui` Calendar) applies hover effects. We must ensure that:
1.  **Status-Specific Hover**: When hovering over a status date, the color should slightly darken/lighten or maintain a high-contrast state.
2.  **Selected State**: When a date is selected, it should have a primary-colored border or a stronger fill to show it is the active choice.
3.  **Global Hover**: The base `day` class uses `hover:bg-foreground hover:text-background`. Status modifiers MUST override this or complement it using `!important` (Tailwind `!`) to ensure the status color remains visible or provides a clear interaction feedback.

## Implementation Details
- Update `STATUS_CONFIG` in `src/components/organisms/types.ts`.
- Ensure `modifier` strings in `types.ts` include the correct hover/active states.
- The `available` status will use `bg-emerald-500 text-white hover:bg-emerald-600`.
- The `limited` status will use `bg-amber-500 text-amber-950 hover:bg-amber-600`.
- The `booked` status will remain disabled (`cursor-not-allowed`) with a strike-through.
