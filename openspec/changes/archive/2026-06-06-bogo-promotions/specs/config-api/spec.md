## MODIFIED Requirements

### Requirement: Global Configuration Fetching
The system MUST provide a way to fetch the global company configuration from the dashboard API, and the services API MUST include promotion fields for each service.

#### Scenario: Fetch configuration from API
1. **Given** the dashboard API is available at `/api/config/`.
2. **When** the `getConfig` utility is called.
3. **Then** it should return an object containing `contact_phone`, `contact_email`, and other branding details.

## ADDED Requirements

### Requirement: Services API Exposes Promotion Fields
The `/api/services/` endpoint SHALL include `buy_x` and `get_y_free` fields in each service object so the frontend can display promotion badges and calculate discounts.

#### Scenario: Service with active promotion
- **WHEN** a service has `buy_x=2` and `get_y_free=1`
- **THEN** the API response for that service SHALL include `buy_x: 2` and `get_y_free: 1`

#### Scenario: Service without promotion
- **WHEN** a service has `buy_x=0` and `get_y_free=0`
- **THEN** the API response SHALL include `buy_x: 0` and `get_y_free: 0`

### Requirement: Availability Endpoints Accept Quantities
The `/api/availability/days/` and `/api/availability/slots/` endpoints SHALL accept an optional `quantities` query parameter (comma-separated integers) parallel to `service_ids`, representing the quantity of each service. When provided, total duration SHALL be computed as `SUM(duration × quantity)` instead of `SUM(duration)`.

#### Scenario: Availability with quantities
- **WHEN** `GET /api/availability/days/?service_ids=1,2&quantities=3,1` is requested
- **AND** Service 1 has `duration_minutes=30` and Service 2 has `duration_minutes=60`
- **THEN** the total duration SHALL be `3×30 + 1×60 = 150` minutes
- **AND** only days with at least 150 minutes of available time SHALL be returned

#### Scenario: Availability without quantities (backward compatible)
- **WHEN** `GET /api/availability/days/?service_ids=1,2` is requested (no `quantities` parameter)
- **THEN** all quantities SHALL default to 1 (existing behavior preserves)

#### Scenario: Availability quantity count mismatch
- **WHEN** `GET /api/availability/days/?service_ids=1,2&quantities=3` is requested
- **THEN** the endpoint SHALL return HTTP 400

#### Scenario: Availability invalid quantity
- **WHEN** `GET /api/availability/slots/?service_ids=1&quantities=0&date=2026-06-10` is requested
- **THEN** the endpoint SHALL return HTTP 400 because quantity must be a positive integer
