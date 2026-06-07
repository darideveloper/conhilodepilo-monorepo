## MODIFIED Requirements

### Requirement: Global Configuration Fetching
The system MUST provide a way to fetch the global company configuration from the dashboard API. The `/api/config/` endpoint SHALL now include the global BOGO promotion fields (`buy_x` and `get_y_free`). The services API no longer returns per-service promotion fields.

#### Scenario: Fetch configuration from API
1.  **Given** the dashboard API is available at `/api/config/`.
2.  **When** the `getConfig` utility is called.
3.  **Then** it should return an object containing `contact_phone`, `contact_email`, `buy_x`, and `get_y_free`.

## ADDED Requirements

### Requirement: Config API Exposes Global Promotion Fields
The `/api/config/` endpoint SHALL include `buy_x` and `get_y_free` fields so the frontend can read the global promotion config.

#### Scenario: Global promotion active
- **WHEN** `CompanyProfile.buy_x=2` and `CompanyProfile.get_y_free=1`
- **THEN** the config API response SHALL include `buy_x: 2` and `get_y_free: 1`

#### Scenario: Global promotion disabled
- **WHEN** `CompanyProfile.buy_x=0` and `CompanyProfile.get_y_free=0`
- **THEN** the config API response SHALL include `buy_x: 0` and `get_y_free: 0`

## REMOVED Requirements

### Requirement: Services API Exposes Promotion Fields
**Reason**: Promotion config is no longer per-service. The `/api/services/` endpoint no longer needs `buy_x`/`get_y_free` fields. The frontend reads these from `/api/config/` instead.
**Migration**: Remove `buy_x` and `get_y_free` from `EventSerializer`. Remove them from the `DashboardService` frontend type.
