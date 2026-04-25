# Design: Move Tour Selector to Start Screen

## Architectural Reasoning
The goal is to improve the logical flow by moving tour selection to the beginning of the booking process. Since the calendar's availability is tour-specific, the user should be prompted to pick a tour before or while selecting a date.

## Component Refactoring
### 1. `BookingFlow.tsx` (The Wrapper)
- **Store Initialization**: Move the `useEffect` that consumes `initialTourId` from the URL here. This "primes" the store before any child component is rendered.
- **Coordination**: No longer just a step toggle; it will now actively ensure the `tourId` is set for Step 1.

### 2. `BookingCalendar.tsx` (Step 1)
- **Tour Selection Integration**:
  - Add the `Select` component at the top of the `CardContent`.
  - Connect the `onValueChange` (or `onChange`) directly to `updateFormData({ tourId: value })`.
  - Because the store is reactive, selecting a tour will immediately update the `availability` modifiers for the `Calendar` and `StatusDetails` without requiring any navigation.
- **Layout**:
  - `Select` (Full width) -> `StatusLegend` -> `Calendar` -> `StatusDetails` -> `Continuar`.

### 3. `BookingForm.tsx` (Step 2)
- **Simplified Form**:
  - Remove the `Tour` selection field entirely.
  - **Grid Layout Refinement**:
    - Row 1: `fullName` (50%) | `email` (50%).
    - Row 2: `guests` (Standalone or paired). Given its size, a full-width input or a 50/50 with another small field could work, but a simple 100% width input is also fine for clarity.
    - Row 3: `specialRequests` (100%).

## State Management (`useBookingStore.ts`)
- **Reactive Availability**: The existing `updateFormData` logic already handles availability recalculation when `tourId` changes. No changes needed to the store itself.
- **Validation**: Ensure that `nextStep` is only allowed if `tourId` is present (usually guaranteed by `initialTourId` or selection) and `selectedDate` is picked.

## Trade-offs
- **Vertical Space in Step 1**: Adding a dropdown to the calendar screen will increase its height slightly. This will be mitigated by reducing vertical gaps in the card structure.
- **Initial Load**: The user may see a brief "Select a tour" state if no ID is provided in the URL, but the default URL-based flow will remain seamless.
