# Tasks: Refactor Availability System

## Phase 1: Data Preparation
- [ ] Update `src/data/tours.json` to add a `dates` object to each tour.
    - [ ] Include `available`, `limited`, and `booked` arrays with sample dates.
- [ ] Update `src/organisms/types.ts` (if needed) to include the `dates` property in the `Tour` interface.

## Phase 2: State Management
- [ ] Refactor `src/store/useBookingStore.ts`:
    - [ ] Add `availability` to the state (derived from selected tour).
    - [ ] Ensure the store updates `availability` whenever `tourId` changes in the form data.

## Phase 3: Component Refactoring
- [ ] Refactor `src/components/organisms/BookingCalendar.tsx`:
    - [ ] Remove hardcoded `bookingData` and relative date helpers.
    - [ ] Retrieve availability from `useBookingStore`.
    - [ ] Update the `modifiers` and `disabled` props of the `Calendar` component to use the store data.
    - [ ] Update `getStatus` and other logic to handle the new date structure.

## Phase 4: Verification
- [ ] Verify that changing the tour in the dropdown updates the calendar's highlighted days.
- [ ] Verify that selecting a date still works correctly and updates `selectedDate` in the store.
- [ ] Verify that the calendar is correctly localized and shows the correct days of the week.
