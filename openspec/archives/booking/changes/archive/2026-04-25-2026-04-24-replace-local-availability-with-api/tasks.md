# Tasks: Replace local availability logic with API integration

- [x] Create API service layer in `src/lib/api/availability.ts` to fetch availability data.
- [x] Update `useBookingStore` types to include `isAvailabilityLoading` and `availabilityError`.
- [x] Remove `getIntersectedAvailability` and `injectVirtualLimitedDates` from `src/store/useBookingStore.ts`.
- [x] Modify `useBookingStore.updateFormData` to trigger `fetchAvailability` when `selectedServices` change.
- [x] Add `AbortController` in the store to handle race conditions during repeated service selections.
- [x] Update `BookingCalendar.tsx` to handle loading/error states from `useBookingStore`.
- [x] Cleanup `src/store/useBookingStore.ts` by removing unused imports and logic.
- [x] Verify functionality with the booking flow.
