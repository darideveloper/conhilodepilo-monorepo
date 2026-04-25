# Spec Delta: API Documentation (Single-Tenant)

## MODIFIED Requirements
### Requirement: API Specification Alignment
The documentation in `docs/apis.md` SHALL reflect a single-tenant backend architecture.

#### Scenario: Update Documentation Content
- **GIVEN** the existing `docs/apis.md`.
- **WHEN** multi-tenancy is removed from the system.
- **THEN** the section "Base URL & Multi-tenancy" MUST be removed.
- **AND** the documentation MUST explicitly state that the `Host` header is no longer used to identify clients.
- **AND** all cURL and JSON examples MUST use the direct API path without client prefixes or custom Host headers.
