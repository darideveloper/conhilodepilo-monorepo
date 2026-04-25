# url-params Specification

## Purpose
TBD - created by archiving change hide-selectors-via-url. Update Purpose after archive.
## Requirements
### Requirement: UI Selector Visibility Control
The application MUST be able to hide language, theme, and service selectors based on the presence of specific URL parameters.

#### Scenario: Hide language selector
- **Given** the user navigates to a URL with `?lang=en`
- **When** the booking flow is rendered
- **Then** the language selector (toggle) MUST NOT be visible
- **And** the language MUST be set to English

#### Scenario: Hide theme selector
- **Given** the user navigates to a URL with `?theme=dark`
- **When** the booking flow is rendered
- **Then** the theme selector (toggle) MUST NOT be visible
- **And** the theme MUST be set to dark

#### Scenario: Hide service selector
- **Given** the user navigates to a URL with `?service=alhambra`
- **When** the booking flow is rendered
- **Then** the service selector dropdown MUST NOT be visible
- **And** the service MUST be set to 'alhambra'

#### Scenario: Support service_group parameter
- **Given** the user navigates to a URL with `?service_group=granada`
- **When** the booking flow is rendered
- **Then** the `service_group` MUST be stored in the application state

#### Scenario: Internal Naming Standardization
The application MUST use `serviceId` internally to refer to the selected service.

- **Given** the selected service is set (via URL or user action)
- **When** the state is accessed or updated
- **Then** it MUST be referenced as `serviceId`

#### Scenario: Visibility reset on reload without params
- **Given** the user was on a URL with `?lang=es` and the language selector was hidden
- **When** the user navigates back to the root URL `/` (without parameters)
- **Then** the language selector MUST be visible again

### Requirement: URL Variable Documentation
All available URL parameters MUST be documented in `docs/url-variables.md`.

#### Scenario: Document all options
- **Given** a new documentation file `docs/url-variables.md` is created
- **When** the user reads it
- **Then** they MUST find clear instructions on how to use `lang`, `theme`, `service`, and `service_group` parameters
- **And** how they affect the UI visibility

### Requirement: URL Variable Support
The application SHALL support the `zoom` URL query parameter to adjust the body zoom level.

#### Scenario: Zooming
- **Given** the user navigates to a URL with `?zoom=120`
- **When** the booking flow is rendered
- **Then** the `body` element shall be styled with `zoom: 120%`
Process Group PGID: 316315

