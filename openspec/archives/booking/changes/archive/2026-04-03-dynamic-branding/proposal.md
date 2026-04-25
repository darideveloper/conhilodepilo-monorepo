# Proposal: Dynamic Branding and Configuration

## Summary
Transition the project from hardcoded branding and static translations to a dynamic configuration system powered by the `GET /config/` API endpoint. This enables tenant-aware branding, including colors, logos, and custom labels, directly from the backend.

## Problem
Currently, the project's visual identity (colors, logo) and specific UI labels (tour labels, availability statuses) are hardcoded or defined in static translation files. This makes it difficult to reuse the frontend for different tour providers (tenants) without manual code changes for each instance.

## Solution
1. **Dynamic Config State:** Update the Zustand store to include a `config` state that stores the data from the `GET /config/` endpoint.
2. **Branding Injection:** Implement a mechanism to dynamically apply the `brand_color` from the API to the project's CSS variables, ensuring all primary UI elements (buttons, accents, focus rings) reflect the provider's brand.
3. **Logo & Business Info:** Update the UI to use the API-provided `logo`, `company_name`, `contact_email`, and `contact_phone`.
4. **Translation Overrides:** Refactor the `useTranslation` hook to support overwriting specific static translation keys with custom labels provided by the API (e.g., changing "Tour" to "Experience" or "Available" to "Free").
5. **Dynamic Routing:** All API calls (starting with `GET /config/`) will be made using a base URL derived from the `PUBLIC_API_URL` environment variable (e.g., `https://darideveloper.com/api/`), with the `client` parameter injected as a subdomain.
6. **Initial Load:** Fetch the configuration on the initial application mount when the `client` parameter is present.

## Scope
- `src/store/useBookingStore.ts`: Add config state and fetch action.
- `src/lib/i18n/useTranslation.ts`: Implement config override logic.
- `src/components/organisms/BookingFlow.tsx`: Handle the initial config fetch and color injection.
- UI Components: Update references to branding assets and business info.
- `openspec/specs/brand-config/`: New requirement for dynamic configuration.
- `openspec/specs/translation/`: New requirement for label overrides.

## Success Criteria
- The application fetches and stores the configuration from `GET /config/` on load.
- The primary brand color of the UI matches the `brand_color` returned by the API.
- The logo and company name displayed reflect the API response.
- UI labels (like "Tour" or status names) are successfully overwritten by API-provided labels when present.
- The application remains functional with its static defaults if the API call fails or specific labels are missing.
