## 1. Setup API Infrastructure
- [x] 1.1 Create `src/lib/api/types.ts` for centralized request/response interfaces.
- [x] 1.2 Create `src/lib/api/client.ts` with base `apiClient`.

## 2. Implement Configuration Service
- [x] 2.1 Create `src/lib/api/endpoints/config.ts` for fetching application configuration (`GET /config/`).
- [x] 2.2 Refactor `useBookingStore.ts` to use `fetchConfig` from the new service layer.
- [x] 2.3 Verify `fetchConfig` successfully updates state and branding during initialization in `BookingFlow.tsx`.
- [x] 2.4 Refactor `Layout.astro` to use the `fetchConfig` service for dynamic server-side branding.

## 3. Implement Booking Service
- [x] 3.1 Create `src/lib/api/endpoints/booking.ts` for submitting booking details (`POST /bookings/` or current Stripe endpoint).
- [x] 3.2 Update `BookingForm.tsx` to call `submitBooking` from the new service layer.
- [x] 3.3 Replace simulated 2-second timeout in `BookingForm.tsx` with a real network call integrated with user feedback.

## 4. Validation and Cleanup
- [x] 4.1 Remove direct `fetch` calls and inline URL construction from `useBookingStore.ts`.
- [x] 4.2 Verify overall flow and error handling performance across the application.
- [x] 4.3 Validate and archive the proposal.
