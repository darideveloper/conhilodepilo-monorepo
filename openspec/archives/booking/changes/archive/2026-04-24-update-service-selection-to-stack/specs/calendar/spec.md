## MODIFIED Requirements
### Requirement: Data Structure Compatibility
The component SHALL consume a simplified availability data structure where availability is inferred.

#### MODIFIED Scenario: Mock Data Integration
- **GIVEN** a `bookingData` structure (e.g. from `useBookingStore`)
- **WHEN** it contains `booked` and `limited` arrays of `Date` objects
- **THEN** any future date not present in these arrays MUST be treated as "available".
- **AND** the availability arrays MUST represent the intersected availability across all stacked services.

## NEW Requirements
### Requirement: Availability Conflict Handling
The system SHALL provide clear feedback when selected services have mutually exclusive availability schedules.

#### Scenario: Conflict Warning Visibility
- **GIVEN** the user has stacked two or more services.
- **WHEN** the intersection of their available dates results in zero (0) open slots.
- **THEN** the application MUST display a clear warning message explaining that the services have conflicting schedules.
- **AND** the UI SHOULD suggest removing a service to resolve the conflict.
