# header Specification

## Purpose
TBD - created by archiving change add-header. Update Purpose after archive.
## Requirements
### Requirement: Website Header
The system SHALL provide a global sticky header across all main pages containing the brand logo, navigation links, and a primary booking call-to-action.

#### Scenario: User navigates on desktop
- **WHEN** the user views the header on a desktop viewport
- **THEN** they see the full horizontal navigation bar with all available page links

#### Scenario: User navigates on mobile
- **WHEN** the user views the header on a mobile viewport
- **THEN** the navigation links are hidden behind a toggleable menu icon (hamburger)

#### Scenario: User clicks to book
- **WHEN** the user clicks the "Reserva Ahora" button
- **THEN** they are directed to the booking flow/URL

