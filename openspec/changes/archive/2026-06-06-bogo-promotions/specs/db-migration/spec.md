## ADDED Requirements

### Requirement: BOGO Promotion Migration
The system SHALL provide a safe staged database migration that adds `buy_x` and `get_y_free` fields to the `Event` model, adds booking price snapshot fields to the `Booking` model, creates the `BookingServiceThrough` model, and migrates existing M2M data.

#### Scenario: Forward migration — new fields
- **WHEN** the migration is applied
- **THEN** the `booking_event` table SHALL have `buy_x` (integer, default=0) and `get_y_free` (integer, default=0) columns
- **AND** the `booking_booking` table SHALL have `original_amount`, `discount_amount`, and `total_amount` (decimal, default=0.00) columns

#### Scenario: Forward migration — through model
- **WHEN** the migration is applied
- **THEN** the `booking_bookingservicethrough` table SHALL be created with columns: `id`, `booking_id`, `event_id`, `quantity`, `unit_price`
- **AND** the table SHALL have a unique constraint on `(booking_id, event_id)`
- **AND** all existing rows in `booking_booking_services` SHALL be migrated to `booking_bookingservicethrough` with `quantity=1` and `unit_price` copied from the related Event price

#### Scenario: Existing booking amount backfill
- **WHEN** the migration backfills existing bookings
- **THEN** `original_amount` and `total_amount` SHALL be set to the sum of migrated through rows (`quantity × unit_price`)
- **AND** `discount_amount` SHALL be set to `0.00`

#### Scenario: Explicit migration strategy
- **WHEN** Django cannot safely auto-generate the through-model transition
- **THEN** the migration SHALL use a staged schema/data migration strategy (for example `SeparateDatabaseAndState`) to preserve existing booking-service relationships

#### Scenario: Backward migration
- **WHEN** the migration is rolled back
- **THEN** the `buy_x`, `get_y_free`, `original_amount`, `discount_amount`, and `total_amount` columns SHALL be removed
- **AND** the `BookingServiceThrough` table SHALL be dropped
- **AND** the `Booking.services` field SHALL revert to using the auto-generated through table
