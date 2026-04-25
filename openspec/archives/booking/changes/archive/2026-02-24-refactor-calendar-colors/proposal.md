# Proposal: Refactor Booking Calendar Colors

This proposal outlines the refactoring of the **Booking Calendar** component and the synchronization of the project's global theme variables to use the official shadcn/ui "Red" theme using OKLCH values.

## Why
The current booking calendar uses a separate set of status colors and hex-based variables that deviate from the intended brand theme. By synchronizing the global CSS variables with the official OKLCH values and refactoring the calendar to use these tokens, we ensure full visual consistency and leverage the power of Tailwind CSS v4's color space.

## What Changes
- Update `src/styles/global.css` to use the provided `oklch` values for both light and dark modes.
- Remove the custom `--status-*` variables from `src/styles/global.css`.
- Update the `BookingCalendar` component to use standard shadcn/ui variables like `primary`, `muted`, `accent`, and `destructive`.
- Re-map the availability statuses to the brand palette using semantic tokens:
    - **Full**: Use `destructive` (which maps to the brand red).
    - **Limited**: Use `muted`.
    - **Available**: Use `primary`.

## Goals
- Achieve 100% visual alignment with the official Granada Go Tours "Red" theme.
- Simplify the CSS configuration by using standardized OKLCH variables.

## Scope
- Styling: `src/styles/global.css` (Full theme update).
- Component: `src/components/BookingCalendar.tsx`.

## Success Criteria
- Global CSS variables match the provided OKLCH reference.
- The calendar uses semantic theme tokens (`primary`, `destructive`, etc.).
- `openspec validate` passes.
