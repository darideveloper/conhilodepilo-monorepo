# Tasks: Dynamic Branding and Configuration

## 1. Store Update
- [x] Update `src/store/useBookingStore.ts`:
    - [x] Add `AppConfig` interface based on API documentation. <!-- id: task-store-interface -->
    - [x] Add `config`, `isConfigLoading`, and `error` to `BookingState`. <!-- id: task-store-state -->
    - [x] Implement `fetchConfig(client: string)` action using `PUBLIC_API_URL` as the base. <!-- id: task-store-action -->
    - [x] Ensure all other API calls (slots, bookings) also use the `PUBLIC_API_URL` base. <!-- id: task-store-api-base -->
    - [x] Ensure `config` is NOT persisted in `localStorage`. <!-- id: task-store-persist -->

## 2. Branding & Logic
- [x] Update `src/components/organisms/BookingFlow.tsx`:
    - [x] Extract `client` parameter from URL. <!-- id: task-flow-client -->
    - [x] Call `fetchConfig(client)` on mount if the client is present. <!-- id: task-flow-fetch -->
    - [x] Implement `useEffect` to inject `brand_color` into CSS variables (`--color-brand-red`, `--primary`). <!-- id: task-flow-color -->
    - [x] Display a loading state or spinner while the initial config is loading (optional, check UX). <!-- id: task-flow-loading -->

## 3. Translation Overrides
- [x] Refactor `src/lib/i18n/useTranslation.ts`:
    - [x] Update the hook to retrieve the `config` from the store. <!-- id: task-i18n-store -->
    - [x] Merge `config` labels into the `t` object, following the mapping defined in the design. <!-- id: task-i18n-merge -->
    - [x] Use `useMemo` to ensure translation stability. <!-- id: task-i18n-memo -->

## 4. UI Component Updates
- [x] Update `src/components/organisms/BookingForm.tsx`:
    - [x] Use `config.logo` for the provider's logo (if logo is present in UI). <!-- id: task-ui-logo -->
    - [x] Use `config.company_name` for business context. <!-- id: task-ui-company -->
- [x] Update `src/components/organisms/BookingCalendar.tsx`:
    - [x] Ensure dropdowns and status legends reflect the overridden labels. <!-- id: task-ui-calendar-labels -->

## 5. Validation
- [x] Mock the `GET /config/` API response and verify:
    - [x] All primary buttons and accents change color to the `brand_color`. <!-- id: task-val-color -->
    - [x] UI labels (Tour, Available, etc.) are correctly overridden. <!-- id: task-val-labels -->
    - [x] The app handles API errors by falling back to static defaults. <!-- id: task-val-fallback -->
- [x] Run `openspec validate dynamic-branding`. <!-- id: task-val-openspec -->
