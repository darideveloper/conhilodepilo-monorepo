## 1. API Integration Setup
- [x] 1.1 Create `src/lib/api/endpoints/services.ts` implementing `fetchServices` utilizing the existing `apiClient` from `src/lib/api/client.ts` (e.g., `apiClient<ServiceCategory[]>("services/")`).
- [x] 1.2 Map the dashboard `ServiceCategory[]` schema safely within the fetching function:
  - Enforce empty `{ limited: [], booked: [] }` defaults for the `dates` property to prevent UI crashes.
  - Coerce all numeric `id` fields (for both categories and services) into `string` values to maintain compatibility with the frontend's strict equality checks.

## 2. Store Migration
- [x] 2.1 Update `BookingState` in `useBookingStore.ts` to include the `services` array and a `fetchServices` action.
- [x] 2.2 Remove the static `import bookingData from "../data/booking.json"` from `useBookingStore.ts`.
- [x] 2.3 Refactor `getInitialAvailability` to read from the dynamically loaded state's `services` instead of the static import.
- [x] 2.4 Update `updateFormData` to rely on the dynamically loaded `services`.

## 3. UI Refactoring
- [x] 3.1 Replace static `bookingData` import with `useBookingStore((state) => state.services)` in `BookingServiceSelection.tsx`.
- [x] 3.2 Refactor `BookingForm.tsx` to read services from the store instead of the static import.
- [x] 3.3 Refactor `BookingCalendar.tsx` to read services from the store instead of the static import.
- [x] 3.4 Refactor `BookingFlow.tsx` to trigger `fetchServices` on mount and replace the static import.
- [x] 3.5 Refactor `[id].astro` to remove `bookingData` and either fetch data server-side or pass the `id` down for the client store to handle.

## 4. Cleanup
- [x] 4.1 Delete the obsolete `src/data/booking.json` file.
- [x] 4.2 Verify availability edge cases (e.g., when the store is still loading) across all booking components.
