# Proposal: Remove Multi-Tenancy Feature

Transition the Booking System from a multi-tenant (white-label) architecture to a single-tenant model to simplify the codebase and align with the primary brand, Granada Go Tours.

## Problem
The system currently supports multiple clients via complex subdomain and query parameter logic. This adds unnecessary overhead to API calls, state management, and documentation, which is not required for a single-brand site.

## Proposed Solution
1.  **Remove Client Identification:** Eliminate the `client` parameter from the store, API URL generation, and the `BookingFlow` component.
2.  **Simplify API Calls:** Standardize on a single base URL for all API interactions without tenant-specific headers or subdomain manipulation.
3.  **Refactor Documentation:** Update `docs/apis.md` and related specs to reflect a single-tenant dashboard.

## Expected Impact
-   **Codebase:** Simpler logic in `useBookingStore.ts`, `Layout.astro`, and `BookingFlow.tsx`.
-   **Maintenance:** Easier to debug API connections without worrying about client-specific routing.
-   **Consistency:** All users see the same brand configuration fetched from a single source.

## Affected Components
-   `src/store/useBookingStore.ts`: `fetchConfig`, `getApiUrl`, and state interfaces.
-   `src/layouts/Layout.astro`: SSR config fetching.
-   `src/components/organisms/BookingFlow.tsx`: Initialization logic.
-   `docs/apis.md`: API specification.
-   `openspec/specs/brand-config/spec.md`: Configuration requirements.
-   `openspec/specs/url-params/spec.md`: URL visibility logic.
-   `openspec/specs/routing/spec.md`: Subdomain requirements.
