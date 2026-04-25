# Design: Transition to Single-Tenant Architecture

This document outlines the architectural changes required to remove the multi-tenancy feature and transition the Booking System to a single-tenant model.

## Rationale
The current system implements complex client identification logic (subdomains, query parameters, `Host` headers) to support multiple brands (white-labeling). For the primary use case of **Granada Go Tours**, this complexity is unnecessary and introduces maintenance overhead. Removing it simplifies the API communication, state management, and configuration loading.

## Architectural Changes

### 1. Centralized Configuration Loading
Currently, configuration is fetched using a `client` identifier.
- **Old Path:** `fetchConfig(client) -> GET http://<client>.<domain>/api/config/`
- **New Path:** `fetchConfig() -> GET http://<domain>/api/config/` (No client identifier).

The backend will serve a single configuration object for the entire deployment.

### 2. Static API URL Generation
The `getApiUrl` utility will no longer manipulate the hostname based on a client ID.
- **Old:** `url.hostname = `${client}.${url.hostname}``
- **New:** `return `${baseUrl}${endpoint}``

### 3. Simplified Component Initialization
The `BookingFlow.tsx` component will no longer look for the `client` query parameter to initialize branding. It will perform a generic fetch on mount.

### 4. Documentation Alignment
The `docs/apis.md` and `docs/url-variables.md` files must be updated to remove any reference to tenant-specific logic, ensuring clarity for developers.

## Trade-offs
- **Cons:** Losing the ability to host multiple brands on a single frontend deployment.
- **Pros:** Reduced code complexity, fewer points of failure in URL construction, and a cleaner codebase aligned with the project's specific purpose.
