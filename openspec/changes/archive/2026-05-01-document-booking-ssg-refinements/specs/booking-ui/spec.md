# spec Delta: Client-Side Zoom Handling

## ADDED Requirements

### Requirement: Dynamic Page Scaling
The application MUST support dynamic scaling via the `zoom` query parameter to ensure proper rendering when embedded in iframes on the landing page.

#### Scenario: Applying zoom in a static environment
- **GIVEN** the application is served as a static site
- **WHEN** a user visits the application with a `?zoom=X` parameter
- **THEN** the system MUST dynamically apply the zoom percentage to the document body via client-side CSS injection
- **AND** the scaling MUST be applied as early as possible to minimize layout shifts.
