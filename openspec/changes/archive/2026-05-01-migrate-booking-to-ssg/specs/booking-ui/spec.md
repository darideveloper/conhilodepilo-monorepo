# spec Delta: Single-Page Static Rendering

## ADDED Requirements

### Requirement: Single-Page Application Mode
The booking application MUST operate as a single-page static site where all routing logic for specific services is handled via URL query parameters rather than separate file-system routes.

#### Scenario: Building a single entry point
- **GIVEN** the booking application source code
- **WHEN** the build command is executed
- **THEN** it MUST only generate a single `index.html` file
- **AND** all other service-specific logic MUST be handled by the client-side bundle.

### Requirement: Unified Service Selection
The system MUST use the `service` query parameter as the primary method for auto-selecting a service upon application load.

#### Scenario: Loading with a service parameter
- **GIVEN** a user visits `/?service=123`
- **WHEN** the React application hydrates
- **THEN** it MUST fetch details for service `123` and pre-select it in the booking flow.
