# Design: Clean Branding and Dynamic Configuration

This document outlines the architectural changes for replacing hardcoded "Granada Go" and "tours" branding with dynamic configuration from the API.

## Architectural Decision: Server-Side Config Fetching in Astro

Astro components render on the server, while the React store (Zustand) hydrates on the client. To avoid a "Flash of Unbranded Content" (FOUC) and ensure SEO meta tags like `<title>` are correct, the config must be fetched on the server in `Layout.astro`.

### Workflow
1.  **Server-Side (Astro)**:
    - Extract `Host` header from `Astro.request`.
    - Fetch `/api/config/` from the API base.
    - Set `<title>`, `<meta>`, and inline CSS variables (e.g., `--brand-color`).
2.  **Client-Side (React)**:
    - The `fetchConfig` action in `useBookingStore.ts` will still fetch config to hydrate the client-side state.
    - Components will use `config` from the store for real-time reactive updates (e.g., logos, button labels).

## Terminology Refactoring: "Tours" → "Services"

The codebase currently uses "Tours" as a primary domain term. The API provides `event_label` (e.g., "Tour", "Booking", "Appointment") and `event_type_label` (e.g., "Tours", "Services").

### Implementation
- **Terminology Mapping**: In `src/lib/i18n/useTranslation.ts`, we will map `config.event_label` to the translation object's labels.
- **CSS Selectors**: Rename selectors like `#tours-cards` to `#service-items` to maintain generic naming conventions.
- **Asset Paths**: Deprecate the `public/tours/` directory. All images should come from the API's `image` field in the `/api/events/` results.

## Removal of Deprecated WordPress Integration

The scripts and styles located in `src/assets/wordpress/` are legacy code used for a previous integration method. Since the project now uses a dynamic configuration approach and is not dependent on these scripts, they will be removed entirely to clean up the codebase.

### Implementation
- Delete all files under `src/assets/wordpress/`.
- Remove any references or imports of these assets in the main codebase (if any).

