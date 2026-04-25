## ADDED Requirements

### Requirement: URL Variable Support
The application SHALL support the `zoom` URL query parameter to adjust the body zoom level.

#### Scenario: Zooming
- **Given** the user navigates to a URL with `?zoom=120`
- **When** the booking flow is rendered
- **Then** the `body` element shall be styled with `zoom: 120%`
Process Group PGID: 316315
