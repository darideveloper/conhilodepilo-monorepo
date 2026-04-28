# booking-ui Specification

## Purpose
TBD - created by archiving change fix-timezone-mismatch. Update Purpose after archive.
## Requirements
### Requirement: Timezone Consistency
The system MUST use `Europe/Madrid` as the primary timezone for business logic and data display.

#### Scenario: Backend Timezone Configuration
- GIVEN the backend application environment variables
- THEN the `TIME_ZONE` MUST be configured as `Europe/Madrid`.

### Requirement: Accurate Availability Display
The booking calendar MUST display available days exactly as returned by the API, without 1-day shifts due to client-side timezone offsets.

#### Scenario: Parsing Availability Dates
- GIVEN a list of available date strings in "YYYY-MM-DD" format from the API
- WHEN the frontend parses these strings into `Date` objects
- THEN it MUST parse them as local dates (e.g., using `new Date(year, month, day)`) to avoid UTC-to-local shifts.

### Requirement: Persistent Date Integrity
The application MUST maintain the correct selected date after page refreshes, regardless of the user's timezone offset.

#### Scenario: Rehydrating Selected Date
- GIVEN a stored selected date
- WHEN the application rehydrates its state from local storage
- THEN the revived `Date` object MUST represent the same calendar day as originally selected.

