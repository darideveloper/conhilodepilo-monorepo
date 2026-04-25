# calendar Specification Delta

## MODIFIED Requirements
### Requirement: Data Structure Compatibility
The component SHALL consume a simplified availability data structure where availability is inferred.

#### MODIFIED Scenario: Mock Data Integration
- **GIVEN** a `bookingData` structure (e.g. from `useBookingStore`)
- **WHEN** it contains `booked` and `limited` arrays of `Date` objects
- **THEN** any future date not present in these arrays MUST be treated as "available".
- **AND** all specified exception dates MUST be correctly mapped to their respective modifiers in the calendar component.

#### MODIFIED Scenario: Status Keys Consistency
- **GIVEN** the `STATUS_CONFIG` object
- **WHEN** statuses are assigned
- **THEN** the keys MUST be `available`, `limited`, and `booked` (for exceptions), and `standard` (for non-future dates).
