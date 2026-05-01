# availability-logic Specification

## Purpose
TBD - created by archiving change fix-availability-intersection. Update Purpose after archive.
## Requirements
### Requirement: O(1) Database Query Performance per Date Check
The dashboard `get_available_dates` calculation MUST gather all necessary date override, availability range, and weekday slot constraints in bulk. The iterations checking daily availability over the 30-day period MUST execute entirely in memory and MUST NOT execute any database queries inside the per-date loop or per-service loop.

#### Scenario: Validating N+1 query elimination
- **Given** the dashboard has 5 services with various availability slots and overrides.
- **When** the client requests available dates for 3 services spanning 30 days.
- **Then** the total number of database queries executed by `get_available_dates` MUST be constant and strictly lower than 10 (irrespective of the 30 days or 3 services).

