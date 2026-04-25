# Spec Delta: brand-config (Single-Tenant)

## MODIFIED Requirements
### Requirement: Static Configuration Initialization
The application SHALL fetch and store its branding and business configuration from the `GET /config/` API endpoint on initial load from the primary backend host.

#### Scenario: Successful Configuration Load
- **GIVEN** the application is mounting.
- **WHEN** the request is made to the static `/api/config/` endpoint and returns a successful response.
- **THEN** the application MUST store the configuration in its global state.
