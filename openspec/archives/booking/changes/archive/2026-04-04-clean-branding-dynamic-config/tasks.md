# Tasks: Clean Branding and Dynamic Configuration

This document outlines the ordered list of tasks for removing hardcoded branding and implementing dynamic configuration from the API.

## Implementation Tasks

### 1. Astro Server-Side Configuration
- [x] **Astro Layout**: Fetch `/api/config/` on the server in `src/layouts/Layout.astro`.
- [x] **Metadata**: Update `<title>` to use `config.company_name` or a generic fallback.
- [x] **CSS Variables**: Set `--brand-color` and `--primary` directly in the `<head>` to avoid FOUC.
- [x] **Loader**: Replace "Granada Go" in `src/components/atoms/AppLoader.astro` with a generic loading icon or `config.company_name`.

### 2. Terminology and Translation
- [x] **Translations**: Remove "Granada Go Tours" from English and Spanish titles in `src/lib/i18n/translations.ts`.
- [x] **Hook Update**: Ensure `src/lib/i18n/useTranslation.ts` fully utilizes `config.event_label` and `config.event_type_label`.
- [x] **Generic Terms**: Update all components (`BookingForm.tsx`, `BookingCalendar.tsx`, etc.) to use these dynamic labels instead of hardcoded "Tour".

### 3. WordPress Integration Removal
- [x] **Remove Files**: Delete all files in `src/assets/wordpress/`.
- [x] **Cleanup Selectors**: Ensure that any CSS selectors that were shared with these scripts are genericized or removed if unused.
- [x] **References**: Verify that no other parts of the application reference these deprecated assets.

### 4. Codebase Cleanup
- [x] **CSS/Classes**: Search and replace "tours" with "services" or "events" in non-functional class names and IDs across the codebase.
- [x] **Deprecation**: Mark `public/tours/` directory for deletion (to be removed once the events API is fully integrated).

## Validation Tasks
- [x] **Smoke Test**: Verify that the application title and colors are dynamic by mocking different API responses.
- [x] **Integration Test**: Confirm the WordPress scripts work when the `Host` header is overridden.
- [x] **Build Check**: Ensure no hardcoded "Granada Go" or "tours" strings remain in user-visible text.
