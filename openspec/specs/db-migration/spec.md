# db-migration Specification

## Purpose
TBD - created by archiving change migrate-db-to-prod. Update Purpose after archive.
## Requirements
### Requirement: DB-MIG-001 - Automated Data Transfer
The system SHALL provide a mechanism to export the database from the source environment and import it into the target environment using standard PostgreSQL tools.

#### Scenario: Exporting local data
Given a configured `.env.dev` file
When the migration script is executed with the `export` command
Then it should create a `db_migration.bak` file containing the local database state.

#### Scenario: Importing to production
Given a valid `db_migration.bak` file and a configured `.env.prod` file
When the migration script is executed with the `import` command
Then it should restore the data to the production database, overwriting existing tables but maintaining structural integrity.

### Requirement: DB-MIG-002 - Security and Privacy
The migration process MUST ensure that sensitive credentials are never exposed in logs, console output, or temporary files that persist beyond the migration.

#### Scenario: Protecting credentials
Given the migration process
When commands are executed
Then no passwords or sensitive hosts should be printed to the console or stored in log files.

#### Scenario: Temporary File Management
Given the creation of a database dump
When the migration is completed (successfully or with error)
Then the temporary dump file should be removed unless a specific flag is provided to keep it.

### Requirement: DB-MIG-003 - Post-Migration Consistency
After the data import, the system MUST ensure that the database is in a consistent state, including schema alignment and sequence synchronization.

#### Scenario: Sequence Reset
Given a successful database import
When the sequence reset step is executed
Then all PostgreSQL sequences should be synchronized with the current maximum values in their respective tables.

### Requirement: DB-MIG-004 - Production Safety Backup
Before any data is imported into the production database, a backup of the current production state MUST be created.

#### Scenario: Pre-migration backup
Given a configured `.env.prod` file
When the migration script starts the import process
Then it should first create a `prod_backup_$(date).bak` file.

### Requirement: DB-MIG-005 - Media Asset Synchronization
The migration process SHALL include a mechanism to synchronize media assets from the local environment to the production storage (S3 or local filesystem).

#### Scenario: Uploading to S3
Given `STORAGE_AWS=True` in `.env.prod`
When the media sync step is executed
Then local media files should be uploaded to the specified S3 bucket.

### Requirement: DB-MIG-006 - BOGO Promotion Schema Migration
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

