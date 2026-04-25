# Data Fetching Specification

## MODIFIED Requirements

### Requirement: Centralized API Layer
The application MUST encapsulate external data retrieval in dedicated API scripts within the `src/lib/api/` directory to decouple data fetching from UI components.

#### Scenario: Fetching domain data
- **WHEN** the application requires data for services or courses
- **THEN** it retrieves this data by invoking domain-specific async functions (e.g., `getServices()`, `getCourses()`) located in `src/lib/api/` which fetch from `[PUBLIC_API_URL]/api/services/`.
- AND the components receive strongly typed, normalized data objects.
- AND the data is split appropriately: index 0 is mapped to Courses, and the remaining categories are mapped to Services.
