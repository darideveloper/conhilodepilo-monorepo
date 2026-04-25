# brand-config Specification

## Purpose
TBD - created by archiving change setup-brand-environment. Update Purpose after archive.
## Requirements
### Requirement: Visual Identity Tokens
The project SHALL have a consistent visual identity derived from a single brand color and supporting primary/secondary/accent tones.

#### Scenario: Define Unified Brand Color
- Given the primary Brand Red color: `oklch(0.577 0.245 27.325)`.
- When this is defined as the primary source for `--color-brand-red` and mapped to `--primary`.
- Then all primary UI elements MUST automatically inherit this color.

### Requirement: Theme Switching System
The system SHALL provide a mechanism for users to switch between Light and Dark themes.

#### Scenario: Toggle Theme
- Given a user viewing the application.
- When they interact with the theme toggle component.
- Then the application MUST flip between `.light` (default) and `.dark` mode instantly.

#### Scenario: Persist Theme Preference
- Given a user has selected a specific theme.
- When they revisit the site or reload the page.
- Then the application MUST load the saved theme from `localStorage` before rendering to avoid flashes.

### Requirement: Dynamic Configuration Initialization
The application SHALL fetch and store its branding and business configuration via the **centralized API Service Layer** on initial load, using the `client` URL parameter as a subdomain for the API call.

#### Scenario: Successful Configuration Load with Subdomain
- **GIVEN** the application is mounting in `BookingFlow.tsx`.
- **AND** the URL contains `?client=company1`.
- **WHEN** the `fetchConfig` service is called with the identifier.
- **THEN** it MUST perform a request to `http://company1.api-base-host/api/config/` and returns a successful response.
- **AND** the application MUST store the configuration in its global store.

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

### Requirement: Dynamic Page Branding
The application MUST use branding and metadata from the API to set the page title, logo, and brand colors.

#### Scenario: Set Dynamic Page Title
- **GIVEN** a request to the application.
- **WHEN** the server fetches the config from `/api/config/`.
- **THEN** the `<title>` tag in the `<head>` MUST be set to the `company_name` value from the API.

#### Scenario: Set Dynamic Brand Color
- **GIVEN** a request to the application.
- **WHEN** the server or client fetches the config from `/api/config/`.
- **THEN** the CSS variables `--brand-color` and `--primary` MUST be updated to the `brand_color` value from the API.

#### Scenario: Set Dynamic App Logo
- **GIVEN** a request to the application.
- **WHEN** the config from `/api/config/` is available.
- **THEN** components displaying a logo MUST use the `logo` URL from the API.

### Requirement: Generic Terminologies
The application MUST use labels provided by the API instead of hardcoded terms like "Tour".

#### Scenario: Dynamic Event Labels
- **GIVEN** a config from `/api/config/` containing `event_label` and `event_type_label`.
- **WHEN** displaying labels for services or events in the UI.
- **THEN** the UI MUST use the values from the API (e.g., "Booking", "Appointment") instead of hardcoded "Tour".

