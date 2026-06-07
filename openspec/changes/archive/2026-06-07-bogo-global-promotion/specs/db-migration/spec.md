## MODIFIED Requirements

### Requirement: DB-MIG-006 - BOGO Promotion Migration to Global Config
The system SHALL provide a forward migration (`0017`) that moves BOGO promotion fields from the per-service `Event` model to the global `CompanyProfile` singleton. This migration removes `buy_x`/`get_y_free` from Event and adds them to CompanyProfile.

#### Scenario: Forward migration — remove from Event, add to CompanyProfile
- **WHEN** migration `0017` is applied
- **THEN** the `booking_event` table SHALL lose the `buy_x` and `get_y_free` columns
- **AND** the `booking_companyprofile` table SHALL gain `buy_x` (integer, default=0) and `get_y_free` (integer, default=0) columns

#### Scenario: No data migration needed
- **WHEN** migration `0017` is applied
- **THEN** existing per-service promotion values on Event SHALL be discarded
- **AND** the admin SHALL configure the global promotion value after deployment via CompanyProfileAdmin

#### Scenario: Backward migration (rollback)
- **WHEN** migration `0017` is rolled back
- **THEN** the `buy_x` and `get_y_free` columns SHALL be removed from `booking_companyprofile`
- **AND** the `buy_x` and `get_y_free` columns SHALL be re-added to `booking_event` with default=0
- **AND** no per-service values can be recovered (they were discarded on forward migration)
