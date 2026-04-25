## 1. State Management Updates
- [x] 1.1 Update `BookingState['formData']` in `useBookingStore.ts` to use `selectedServices: Array<{serviceTypeId: string, serviceId: string}>`.
- [x] 1.2 Implement legacy state migration in `onRehydrateStorage` to convert old `serviceId` strings into the new array format.
- [x] 1.3 Refactor `getInitialAvailability` to perform date intersection across multiple services.

## 2. UI Updates
- [x] 2.1 Refactor `BookingServiceSelection.tsx` to include an "Add to Booking" button and a visual list of currently stacked services.
- [x] 2.2 Implement "Availability Conflict" warning in `BookingCalendar.tsx` or `BookingFlow.tsx` when intersection yields zero dates.
- [x] 2.3 Update `BookingForm.tsx` to display a comprehensive list of all stacked services in the summary area.

## 3. API Integration Updates
- [x] 3.1 Update the `BookingPayload` interface in `src/lib/api/endpoints/booking.ts` to use `serviceIds: string[]`.
- [x] 3.2 Update `BookingForm.tsx` submission logic to map the `selectedServices` array into the `serviceIds` payload format.
- [x] 3.3 Ensure URL parameter initialization in `BookingFlow.tsx` is idempotent (prevents duplicate additions).
