# Spec Delta: Database Migration Requirements

## ADDED Requirements

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
