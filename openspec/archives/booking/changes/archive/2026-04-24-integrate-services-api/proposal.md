# Proposal: integrate-services-api

## Why
Currently, the `daridev-cal-booking` frontend retrieves service and category data via a synchronous import of `booking.json`. This static data limits dynamic behavior and does not represent the real data source. Transitioning to a dynamic, asynchronous API-driven architecture ensures that the application operates on the latest data and accurately reflects the backend schema.

## What Changes
We will replace the local static dummy data (`src/data/booking.json`) with real data sourced from the Django backend API (`/api/services/`), migrating from synchronous imports to asynchronous state management without breaking existing component behavior.

## Context
This static data is heavily integrated across the application:
1. Imported directly in `useBookingStore.ts` for synchronous availability lookups (`getInitialAvailability`).
2. Imported directly in UI components (`BookingForm.tsx`, `BookingServiceSelection.tsx`, `BookingCalendar.tsx`, `BookingFlow.tsx`) and the Astro page `[id].astro`.

The new architecture requires this data to be fetched asynchronously from a live Django backend API, returning a nested structure where `ServiceCategory` contains an array of `Service` items. 

### Critical Data Discrepancies
1. **Missing Availability Dates:** The new backend payload does not currently provide `dates` (limited/booked) within the service payload, requiring safe fallback handling.
2. **ID Type Mismatch:** The frontend currently expects IDs (`serviceId`, `serviceTypeId`) to be `string` values, which are used in strict equality checks (`s.id === serviceId`). The backend API provides IDs as `number` values.
3. **Unused Fields:** The backend omits several dummy fields (`meta_title`, `meta_description`, `faqs`). Codebase analysis confirms these are not utilized in the UI, requiring no complex mapping.

The project recently implemented a centralized API client infrastructure (`apiClient`). This feature MUST strictly adhere to this architecture.

## Solution
1. **API Client Integration:** Create `src/lib/api/endpoints/services.ts` utilizing the existing `apiClient` (`src/lib/api/client.ts`) to fetch from the `services/` endpoint.
2. **Data Mapping & Type Coercion:** At the API fetch layer, automatically map numeric backend IDs to strings to maintain strict equality compatibility across the UI. Inject fallback `dates` arrays.
3. **State Management Migration:** Update `useBookingStore.ts` to:
   - Add `services` to the Zustand state.
   - Implement an async `fetchServices()` action (following the pattern of `fetchConfig`).
   - Refactor `getInitialAvailability` to read from the dynamically loaded state.
4. **Component Updates:** Refactor all components and pages importing `booking.json` to instead subscribe to `useBookingStore((state) => state.services)` or receive it via props in the Astro page.
5. **Cleanup:** Remove `src/data/booking.json` entirely.
