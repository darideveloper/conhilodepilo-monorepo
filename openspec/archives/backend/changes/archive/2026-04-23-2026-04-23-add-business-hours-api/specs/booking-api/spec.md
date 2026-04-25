# booking-api Specification

## Purpose
TBD - created by proposal 2026-04-23-add-business-hours-api.

## ADDED Requirements

### Requirement: Business Hours Endpoint
The system MUST provide a public API endpoint to retrieve global operating hours.

#### Scenario: Requesting Business Hours
- GIVEN a client requests `GET /api/business-hours/`
- WHEN the request is processed
- THEN the system MUST return an HTTP 200 OK status
- AND the response MUST be a JSON array containing objects with `weekday`, `start_time`, and `end_time` fields representing the company's `CompanyWeekdaySlot` records.
- AND the endpoint MUST be publicly accessible without authentication.

### Requirement: Bruno Collection Synchronization
All API endpoints MUST have a corresponding request defined in the Bruno collection.

#### Scenario: Exploring Business Hours API
- GIVEN the Bruno collection in `bruno/`
- WHEN a developer inspects the "Booking" folder
- THEN there MUST be a "Get Business Hours" request file configured to query `/api/business-hours/`.