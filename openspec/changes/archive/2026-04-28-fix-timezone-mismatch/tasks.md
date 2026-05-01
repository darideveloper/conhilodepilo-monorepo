# Tasks: Fix Timezone Mismatch

- [x] 1.1 Update `TIME_ZONE` to `Europe/Madrid` in `dashboard/.env` (and check `.env.dev`, `.env.prod` examples).
- [x] 1.2 Update `fetchAvailability` in `booking/src/lib/api/availability.ts` to use local date parsing.
- [x] 1.3 Remove redundant `dateObj > today` logic in `booking/src/components/organisms/BookingCalendar.tsx` to rely entirely on API availability.
- [x] 1.4 Update `onRehydrateStorage` in `booking/src/store/useBookingStore.ts` to ensure `selectedDate` is revived correctly without timezone shifts.
- [x] 1.5 Verify the fix by checking that "YYYY-MM-DD" dates from the API are rendered correctly in the calendar without a 1-day shift and persist correctly after page refresh.
