# Specification: Availability Logic Intersection

## Context
This specification outlines the expected behavior when computing available booking dates for multiple services across a 30-day window via `GET /api/booking/available-days/` and its underlying function `get_available_dates`.

## ADDED Requirements

### Requirement: Mutual Availability Intersection
When calculating available dates for a list of `service_ids`, the system MUST only return a date if **all** the requested services are independently available on that specific date. A `DateOverride` granting availability to one service MUST NOT circumvent the availability checks for the remaining selected services.

#### Scenario: Date override for one service should not bypass unavailability for another
- **Given** Service A is configured to be available from 01/01/2026 to 10/01/2026.
- **And** Service A has a specific positive `EventDateOverride` for 15/01/2026.
- **And** Service B is configured to be available from 05/01/2026 to 10/02/2026 and has no specific overrides.
- **When** the client requests available dates for both Service A and Service B starting from 01/01/2026.
- **Then** the intersection MUST NOT include 15/01/2026, as Service B is not explicitly configured to be available on that day.
- **And** the result should only contain dates from 05/01/2026 to 10/01/2026.

## ADDED Requirements

### Requirement: O(1) Database Query Performance per Date Check
The dashboard `get_available_dates` calculation MUST gather all necessary date override, availability range, and weekday slot constraints in bulk. The iterations checking daily availability over the 30-day period MUST execute entirely in memory and MUST NOT execute any database queries inside the per-date loop or per-service loop.

#### Scenario: Validating N+1 query elimination
- **Given** the dashboard has 5 services with various availability slots and overrides.
- **When** the client requests available dates for 3 services spanning 30 days.
- **Then** the total number of database queries executed by `get_available_dates` MUST be constant and strictly lower than 10 (irrespective of the 30 days or 3 services).
