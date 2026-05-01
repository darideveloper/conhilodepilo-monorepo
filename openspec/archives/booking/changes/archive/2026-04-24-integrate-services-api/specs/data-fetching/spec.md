# data-fetching Specification

## ADDED Requirements

### Requirement: Centralized API Layer and Async State Management
The application MUST encapsulate external data retrieval in dedicated API scripts within the `src/lib/api/endpoints/` directory. All new API scripts MUST use the centralized `apiClient` for consistency and decoupling from UI components.

#### Scenario: Fetching domain data
- **WHEN** the application requires data for services
- **THEN** it retrieves this data by invoking `fetchServices()` which utilizes the centralized `apiClient` to perform a GET request to the `services/` endpoint.
- AND the raw data is safely mapped to provide fallback structures (like empty `dates` for availability) if missing from the dashboard response.
- AND the UI components reactively read the `services` list from the `useBookingStore` rather than relying on synchronous static JSON imports.
