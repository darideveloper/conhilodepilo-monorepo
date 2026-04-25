# brand-config Spec Delta

## ADDED Requirements

### Requirement: Dynamic Configuration Initialization
The application SHALL fetch and store its branding and business configuration from the `GET /config/` API endpoint on initial load, using the `client` URL parameter as a subdomain for the API call.

#### Scenario: Successful Configuration Load with Subdomain
- **GIVEN** the application is mounting.
- **AND** the URL contains `?client=company1`.
- **WHEN** the request is made to `http://company1.api-base-host/api/config/` and returns a successful response.
- **THEN** the application MUST store the configuration in its global state.

### Requirement: Dynamic Brand Color Injection
The application SHALL dynamically update its primary brand color based on the `brand_color` value returned by the configuration API.

#### Scenario: Verify Primary Color Injection
- **GIVEN** a configuration object with `brand_color: "#a01313"`.
- **WHEN** the configuration is loaded.
- **THEN** the `--color-brand-red` and `--primary` CSS variables on the root element MUST be updated to `#a01313`.

### Requirement: Brand Color Validation
The application SHALL validate that the `brand_color` provided by the API is a valid CSS color string before applying it to the document's styles.

#### Scenario: Invalid Brand Color Fallback
- **GIVEN** a configuration object with an invalid `brand_color` (e.g., "javascript:alert(1)").
- **WHEN** the configuration is loaded.
- **THEN** the application MUST NOT apply this value to the CSS variables.
- **AND** the application MUST fall back to the default brand colors defined in `global.css`.

### Requirement: Business Context Branding
The application SHALL use the API-provided `logo` and `company_name` for its header and identification sections.

#### Scenario: Verify Logo Update
- **GIVEN** a configuration object with a `logo` URL.
- **WHEN** the configuration is loaded.
- **THEN** the application's logo components MUST use the provided URL.
