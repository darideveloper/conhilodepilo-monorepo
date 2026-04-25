# components Specification

## MODIFIED Requirements

### Requirement: Service Presentation
The system SHALL present services grouped by their respective categories using an interactive card interface that aligns with the brand's visual identity.

#### Scenario: Interacting with service pills
- **WHEN** the user hovers over a service selection button
- **THEN** the cursor MUST change to a pointer to indicate interactability.

#### Scenario: Interacting with the booking button
- **WHEN** the user hovers over the "Reservar" button
- **THEN** the cursor MUST change to a pointer.

## ADDED Requirements

### Requirement: Booking Redirection
The system SHALL ensure that users entering the booking flow have a valid service selected.

#### Scenario: Accessing booking without a service ID
- **WHEN** a user navigates directly to `/booking` without an `id` query parameter
- **THEN** the system MUST redirect them to the homepage (`/`).
