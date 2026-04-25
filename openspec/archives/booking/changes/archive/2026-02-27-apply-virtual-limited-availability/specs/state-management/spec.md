# state-management Specification Delta

## ADDED Requirements
### Requirement: Virtual Availability Injection
The state management system SHALL dynamically supplement tour availability data with a "Virtual Limited" window during initialization.

#### Scenario: Inject Virtual Limited Dates
- **GIVEN** a tour is selected.
- **WHEN** availability is loaded from the data source.
- **THEN** the `availability.limited` state MUST be merged with the next 10 days relative to the current time.
- **AND** dates already present in `availability.booked` MUST NOT be overwritten by the limited status.
