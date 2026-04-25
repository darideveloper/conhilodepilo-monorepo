# Capability: Brand Configuration

This capability handles the retrieval and application of tenant-specific branding and configuration from the API.

## ADDED Requirements

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
