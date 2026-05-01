## MODIFIED Requirements
### Requirement: Create Booking Endpoint
The system MUST provide an API endpoint to create a new booking record, as defined in the dashboard API contract (`dashboard/openspec/specs/api-contracts/`).

#### Scenario: Successful booking creation
- **WHEN** a valid JSON payload containing user details, selected date/time, and services is submitted
- **THEN** the API MUST create a booking record with status PENDING, accurately calculate the end time based on the selected services, and return a success response.
