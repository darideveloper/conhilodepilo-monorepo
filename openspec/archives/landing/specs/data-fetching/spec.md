# data-fetching Specification

## Purpose
TBD - created by archiving change refactor-data-fetching. Update Purpose after archive.
## Requirements
### Requirement: Centralized API Layer
The application MUST encapsulate external data retrieval in dedicated API scripts within the `src/lib/api/` directory to decouple data fetching from UI components.

#### Scenario: Fetching domain data
- **WHEN** the application requires data for services or courses
- **THEN** it retrieves this data by invoking domain-specific async functions (e.g., `getServices()`, `getCourses()`) located in `src/lib/api/` which fetch from `[PUBLIC_API_URL]/api/services/`.
- AND the components receive strongly typed, normalized data objects.
- AND the data is split appropriately: index 0 is mapped to Courses, and the remaining categories are mapped to Services.

### Requirement: Resilient Data Fetching
The API layer MUST handle failures gracefully to prevent application crashes.

#### Scenario: API Endpoint Failure
- **WHEN** the dummy API endpoint is unreachable or fails to return valid data
- **THEN** the fetching function catches the error and returns an empty array `[]` (or a safe fallback state) to the caller.

