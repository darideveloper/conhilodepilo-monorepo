# Proposal: Centralize Booking State with Zustand

This proposal outlines the transition from local component state to a centralized state management system using Zustand. This will allow the selected booking date and future form data to be accessible across different components and pages.

## Why
Currently, the `BookingCalendar` component manages its own `date` state locally. As the application grows to include a full booking form (contact info, tour selection, etc.), we need a way to:
- Persist user selections as they navigate between steps.
- Share the selected date with other UI elements (e.g., a "Summary" sidebar or the final checkout form).
- Simplify the `BookingCalendar` component by offloading state logic.

## What Changes
- **Dependency Addition**: Install `zustand`.
- **Store Implementation**: Create a `src/store/useBookingStore.ts` to manage the booking process state.
- **Component Refactor**: Update `src/components/BookingCalendar.tsx` to read from and write to the Zustand store instead of using `React.useState`.
- **State Schema**: Define a flexible state object that can eventually hold user details, tour preferences, and the selected date.

## Goals
- Decouple state management from UI components.
- Enable cross-component state sharing.
- Provide a scalable foundation for a multi-step booking process.

## Scope
- New dependency: `zustand`.
- New file: `src/store/useBookingStore.ts`.
- Refactored file: `src/components/BookingCalendar.tsx`.

## Success Criteria
- The selected date is stored in the Zustand store.
- The `BookingCalendar` correctly reflects the state from the store.
- The store is structured to allow easy addition of other form fields (name, email, etc.).
- `openspec validate` passes.
