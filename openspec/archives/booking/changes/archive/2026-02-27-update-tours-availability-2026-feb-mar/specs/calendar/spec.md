# calendar Specification Delta

## MODIFIED Requirements

### Requirement: Data Structure Compatibility
The component SHALL consume a standardized availability data structure that aligns with the backend/JSON schema.

#### Scenario: Mock Data Integration
- **GIVEN** a `bookingData` structure (e.g. from `useBookingStore`)
- **WHEN** it contains `booked`, `limited`, and `available` arrays of `Date` objects
- **THEN** all specified dates MUST be correctly mapped to their respective modifiers in the calendar component.

#### Scenario: Status Keys Consistency
- **GIVEN** the `STATUS_CONFIG` object
- **WHEN** statuses are assigned
- **THEN** the keys MUST be `available`, `limited`, `booked`, and `standard`.
