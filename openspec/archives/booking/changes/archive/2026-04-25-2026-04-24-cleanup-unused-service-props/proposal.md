# Proposal: Cleanup Unused Service Props in Booking Components

## Why
The application currently handles URL-based service pre-selection entirely on the client-side via `BookingFlow.tsx`. The `initialServiceId` prop being passed down through the booking component hierarchy is unused by the rendering logic and is redundant, increasing code complexity.

## What Changes
We will remove the `initialServiceId` prop from `src/components/pages/index.astro` and `src/components/organisms/BookingFlow.tsx`.

## Scope
- `src/components/pages/index.astro`
- `src/components/organisms/BookingFlow.tsx`

## Risks and Mitigation
- **Risk**: Potential dependency on `initialServiceId` that was missed.
- **Mitigation**: Codebase search confirms no active utilization of `initialServiceId` for dynamic routing or server-side pre-selection.
