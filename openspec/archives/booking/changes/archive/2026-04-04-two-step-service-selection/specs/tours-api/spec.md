# Spec Delta: Tours API Removal

## REMOVED Requirements

### Requirement: Serve tour data as JSON
The application SHALL provide a GET endpoint at `/api/tours.json` that returns a JSON array of tours.

#### Scenario: Successful API Request
- **GIVEN**: The tour data is copied to `src/data/tours.json`
- **WHEN**: A client makes a GET request to `/api/tours.json`
- **THEN**: The server responds with a 200 OK status
- **AND**: The response header `Content-Type` is `application/json`
- **AND**: The response body contains the JSON array from `src/data/tours.json`