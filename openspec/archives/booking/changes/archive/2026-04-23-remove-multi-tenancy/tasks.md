# Tasks: Remove Multi-Tenancy

## Phase 1: Core Logic Refactoring
- [x] 1.1 Update `src/store/useBookingStore.ts`:
    - Simplify `getApiUrl` to remove client subdomain logic.
    - Remove `client` parameter from `fetchConfig`.
    - Update `BookingState` interface to remove any client-specific trackers if present.
- [x] 1.2 Update `src/layouts/Layout.astro`:
    - Remove `host` extraction from headers.
    - Fetch config from static `/api/config/` endpoint without the `Host` header.
- [x] 1.3 Update `src/components/organisms/BookingFlow.tsx`:
    - Remove `useEffect` logic that handles the `client` query parameter.
    - Trigger `fetchConfig()` without arguments on mount.
- [x] 1.4 Configuration Environment Check:
    - Verify that `PUBLIC_API_URL` (if set) points to the correct single-tenant dashboard endpoint.

## Phase 2: Specification Updates
- [x] 2.1 Modify `openspec/specs/brand-config/spec.md`:
    - Remove requirements for subdomain-based API calls.
    - Update scenarios to focus on static initialization.
- [x] 2.2 Modify `openspec/specs/url-params/spec.md`:
    - Remove documentation of the `client` parameter.
- [x] 2.3 Modify `openspec/specs/routing/spec.md`:
    - Ensure no requirements imply subdomain routing for tenancy.

## Phase 3: Documentation Cleanup
- [x] 3.1 Update `docs/apis.md`:
    - Remove "Base URL & Multi-tenancy" section.
    - Explicitly state that the `Host` header is no longer used for tenant identification.
    - Update all examples to use a single-tenant structure.
- [x] 3.2 Update `docs/url-variables.md`:
    - Remove the `client` parameter from the list of available variables.

## Phase 4: Validation
- [x] 4.1 Verify branding loads correctly without any URL parameters.
- [x] 4.2 Run `openspec validate remove-multi-tenancy --strict` to ensure spec consistency.
