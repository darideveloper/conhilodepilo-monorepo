## MODIFIED Requirements

### Requirement: Dashboard Service Categorization
The dashboard system MUST allow grouping service categories (Event Types) into broader groups to facilitate filtering and specialization of the booking flow. The `Event` model no longer carries per-service promotion fields — promotion configuration is now global via `CompanyProfile`.

#### Scenario: Assign Group to Event Type
- **Given** an existing `EventType` "Depilación con hilo".
- **And** a group "Salon Services" with ID 1.
- **When** the admin assigns "Salon Services" to "Depilación con hilo".
- **Then** the API MUST return `group_id: 1` for that event type.

## ADDED Requirements

### Requirement: CompanyProfile Promotion Fields
The `CompanyProfile` singleton model SHALL have `buy_x` (PositiveIntegerField, default=0) and `get_y_free` (PositiveIntegerField, default=0) fields to configure a global threshold-style BOGO promotion applied to all services.

#### Scenario: Default values
- **WHEN** a new CompanyProfile is created without specifying promotion fields
- **THEN** `buy_x` SHALL be 0 and `get_y_free` SHALL be 0 (promotion disabled)

#### Scenario: Promotion active globally
- **WHEN** `CompanyProfile.buy_x > 0` and `CompanyProfile.get_y_free > 0`
- **THEN** the promotion SHALL be considered active for ALL services

## REMOVED Requirements

### Requirement: Event Promotion Fields
**Reason**: BOGO promotion fields moved from per-service (`Event`) to global (`CompanyProfile`).
**Migration**: All code that reads `Event.buy_x`/`Event.get_y_free` must be updated to read from `CompanyProfile.get_solo()`. The migration `0017` removes these columns from the `booking_event` table. Per-service values (if any were set) are discarded.
