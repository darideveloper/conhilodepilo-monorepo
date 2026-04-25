## MODIFIED Requirements
### Requirement: Centralized Booking State
The application SHALL manage booking-related data (e.g., selected date, selected services array, user details) in a centralized store to ensure state consistency across components.

#### Scenario: Update Selected Date
- **GIVEN** the application is using a centralized booking store.
- **WHEN** a user selects a date on the `BookingCalendar`.
- **THEN** the `selectedDate` in the centralized store MUST be updated to reflect the choice.

#### Scenario: Add Service to Stack
- **GIVEN** the application is using a centralized booking store.
- **WHEN** a user adds a service to their booking.
- **THEN** the service details MUST be appended to the `selectedServices` array in the store.

### Requirement: Virtual Availability Injection
The state management system SHALL dynamically calculate availability across all selected services and supplement it with a "Virtual Limited" window during initialization.

#### Scenario: Inject Virtual Limited Dates
- **GIVEN** one or more services are selected in the stack.
- **WHEN** availability is loaded from the data source.
- **THEN** the availability MUST be calculated as the intersection of all selected services.
- **AND** the `availability.limited` state MUST be merged with the next 10 days relative to the current time.

## NEW Requirements
### Requirement: Legacy State Migration
The state management system SHALL provide a migration path for users with legacy single-service data in their local storage.

#### Scenario: Rehydrate Legacy State
- **GIVEN** the store is rehydrating from `localStorage`.
- **WHEN** a legacy `serviceId` (string) or `serviceTypeId` (string) is detected in the persisted state.
- **THEN** the system MUST automatically migrate these into a new `selectedServices` array format to prevent application errors.
- **AND** the old single-value fields SHOULD be cleared or ignored after migration.
