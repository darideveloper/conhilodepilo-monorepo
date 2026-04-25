# availability-api Specification

## Purpose
TBD - created by archiving change 2026-04-24-implement-service-availability-api. Update Purpose after archive.
## Requirements
### Requirement: API Endpoint
The system MUST provide a `GET /api/availability/days/` endpoint to query available dates.
#### Scenario: 
- User calls `GET /api/availability/days/?service_ids=1,2`.
- Server returns a JSON list of available dates strings `["2026-04-25", "2026-04-26", ...]`.

### Requirement: Date Range Constraint
The API MUST return dates for the next 30 days only.
#### Scenario:
- Today is `2026-04-24`. 
- The API response contains dates from `2026-04-24` to `2026-05-24`.

### Requirement: Availability Validation
The API MUST only return a date as "available" if there is at least one free slot that fits all selected services.
#### Scenario:
- Service A (60m) and Service B (60m) are requested.
- If a day has only 60m of total availability, it should return "not available".
- If a day has 120m+ of total availability, it should return "available".

