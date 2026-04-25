## Context
This refactor aims to move API calls from state management to a dedicated service layer. This is motivated by the need for a scalable structure that handles consistent error reporting and separates concerns.

## Goals
- Decentralize API logic from the Zustand store.
- Create a predictable response structure for all endpoints.
- Improve type safety using TypeScript interfaces.

## Non-Goals
- Adding new features (like cache/SWR) during the initial refactor.
- Modifying the existing UI/UX during the refactor.

## Decisions

### 1. API Client Strategy
The system will use a base `apiClient` function (or a standard library like `fetch` wrapper) to centralize:
- Base URL resolution (`import.meta.env.PUBLIC_API_URL` fallback).
- Standard request headers.
- Error handling strategies (like log/throwing consistent error objects).

### 2. Service Layer Structure
All API logic will live in `src/lib/api/`:
- `src/lib/api/base.ts`: The generic API requester.
- `src/lib/api/types.ts`: Centralized request/response interfaces for all endpoints.
- `src/lib/api/endpoints/config.ts`: Config-specific endpoint logic (`fetchConfig`).
- `src/lib/api/endpoints/booking.ts`: Booking-specific endpoint logic (`submitBooking`).

### 3. Server-Side vs Client-Side Usage
Since the application uses Astro, some logic runs on the server (e.g., `Layout.astro`). The `apiClient` and services must be usable in both environments (Node.js/Astro server and Browser). 
- **Layout.astro:** Will use the `fetchConfig` service to set the initial document metadata and branding.
- **Client implementation:** Will use standard `fetch` which works in both environments.

## Risks / Trade-offs

None identified at this stage. The main risk of multi-tenant subdomain resolution was mitigated by the recent removal of multi-tenancy from the project.

## Migration Plan
1. Implement the API client and types.
2. Implement the `config` service.
3. Update `useBookingStore.ts` to consume the `config` service.
4. Implement the `booking` service.
5. Replace the simulated submission in `BookingForm.tsx` with the `booking` service.
