# Change: Refactor API Infrastructure

## Why
Currently, API calls are directly embedded in global state management (`useBookingStore.ts`) and simulated in UI components (`BookingForm.tsx`). This mixing of concerns makes the code harder to test, maintain, and refactor. A dedicated API service layer will provide a single source of truth for all network communications and ensure consistent implementation of error handling.

## What Changes
- **API Client:** Implementation of a base API client in `src/lib/api/client.ts` to handle common request logic and base URL resolution.
- **Service Layer:** Movement of specific API calls (`config`, `booking`) into separate dedicated files under `src/lib/api/endpoints/`.
- **Type Safety:** Centralized API request/response types in `src/lib/api/types.ts`.
- **State Integration:** Refactor `useBookingStore.ts` to use the new API service layer.
- **Form Integration:** Replace simulated booking submission in `BookingForm.tsx` with a real API call using the service layer.

## Impact
- Affected specs: `api-service-layer` (New), `booking-submission`, `brand-config`, `state-management`.
- Affected code: `src/store/useBookingStore.ts`, `src/components/organisms/BookingForm.tsx`, `src/lib/api/`.
