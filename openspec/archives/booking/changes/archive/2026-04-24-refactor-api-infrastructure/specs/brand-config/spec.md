# brand-config Specification

## MODIFIED Requirements
### Requirement: Dynamic Configuration Initialization
The application SHALL fetch and store its branding and business configuration via the **centralized API Service Layer** on initial load, using the `client` URL parameter as a subdomain for the API call.

#### Scenario: Successful Configuration Load with Subdomain
- **GIVEN** the application is mounting in `BookingFlow.tsx`.
- **AND** the URL contains `?client=company1`.
- **WHEN** the `fetchConfig` service is called with the identifier.
- **THEN** it MUST perform a request to `http://company1.api-base-host/api/config/` and returns a successful response.
- **AND** the application MUST store the configuration in its global store.
