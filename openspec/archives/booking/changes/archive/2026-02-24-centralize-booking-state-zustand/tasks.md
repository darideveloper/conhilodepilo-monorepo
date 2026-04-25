# Tasks: Centralize Booking State

- [x] **Setup**
    - [x] Install `zustand` using `npm install zustand`.

- [x] **Store Creation**
    - [x] Create `src/store/useBookingStore.ts`.
    - [x] Define the `BookingState` interface.
    - [x] Implement the store with `selectedDate` and `setSelectedDate`.

- [x] **Component Refactor**
    - [x] Update `src/components/organisms/BookingCalendar.tsx` to use `useBookingStore`.
    - [x] Replace `useState` for date with store hooks.
    - [x] Ensure calendar interactions correctly update the store.

- [x] **Validation**
    - [x] Verify that selecting a date in the calendar updates the store state.
    - [x] Verify that the status display correctly reads from the store state.
    - [x] Run `openspec validate centralize-booking-state-zustand`.
