# Tasks: Unify Phone Configuration

- [x] 1. **Setup API and Utilities**
    - [x] 1.1 Add `AppConfig` interface to `landing/src/lib/api/types.ts`.
    - [x] 1.2 Create `landing/src/lib/api/getConfig.ts` to fetch `/api/config/`.
    - [x] 1.3 Create `landing/src/utils/phone.ts` with `formatPhoneForWhatsApp` and `formatPhoneForDisplay` functions.
    - [x] 1.4 Add unit tests for phone formatting utilities (using Vitest).
    - [x] 1.5 Create `landing/src/lib/constants.ts` for unified contact fallbacks.

- [x] 2. **Refactor Global Components**
    - [x] 2.1 Update `WhatsAppButton.astro` to call `getConfig()` and use dynamic phone with unified fallback.
    - [x] 2.2 Update `Footer.astro` to call `getConfig()`, replace hardcoded placeholders with dynamic data/unified fallbacks, and fix Spanish locale.

- [x] 3. **Refactor Page-Specific CTAs**
    - [x] 3.1 Update `landing/src/pages/booking/[id].astro` to fetch configuration data.
    - [x] 3.2 Replace hardcoded WhatsApp link in `booking/[id].astro` with dynamic version and unified fallback.

- [x] 4. **Validation**
    - [x] 4.1 Verify that the footer shows the number from the API response (or unified fallback).
    - [x] 4.2 Verify that all WhatsApp buttons redirect to the correct dynamic number.
    - [x] 4.3 Ensure no hardcoded phone numbers remain in the `landing/src` directory (except in constants).
    - [x] 4.4 Verify that unit tests pass.
