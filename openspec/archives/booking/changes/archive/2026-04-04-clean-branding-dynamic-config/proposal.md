# Proposal: Clean Branding and Dynamic Configuration

This change aims to remove all hardcoded "Granada Go" and "tours" branding from the codebase, replacing it with dynamic data from the `/api/config/` endpoint. This will allow the platform to be fully white-labeled and tenant-aware based on the domain (Host header).

## Objective
- Eliminate hardcoded branding in UI text, titles, and logos.
- Ensure the application title and metadata are dynamic using server-side fetching in Astro.
- Refactor "tours" terminology to more generic terms like "events" or "services" in CSS classes, IDs, and variable names.
- Update WordPress integration scripts to be environment-agnostic.

## Why
Currently, the codebase contains hardcoded branding ("Granada Go" and "tours") which prevents the application from being fully white-labeled or tenant-aware. By fetching the configuration dynamically, we can use the same frontend for multiple tenants.

## What Changes
- **Astro Layout**: Fetch config on the server to set dynamic `<title>` and meta tags.
- **Components**: Replace "Granada Go" in `AppLoader.astro` with a generic or dynamic state.
- **Terminology**: Map API-provided `event_label` and `event_type_label` to the translation system.
- **Styles**: Remove unused/deprecated WordPress-related styles and genericize remaining styles.
- **WordPress Integration**: Remove all files in `src/assets/wordpress/` as they are deprecated and not used.
- **API URLs**: Ensure any remaining API references use dynamic environment variables.

## Verification Plan
- **Manual Verification**: Confirm the page title changes based on the API response.
- **Snapshot Tests**: Ensure the UI renders correctly with different `brand_color` values.
- **Integration Tests**: Verify that `Host` header detection works for different tenants.
