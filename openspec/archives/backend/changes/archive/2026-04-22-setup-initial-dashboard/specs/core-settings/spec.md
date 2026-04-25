# Capability: Core Settings

## ADDED Requirements

### Requirement: Dynamic Settings Initialization
The `settings.py` SHALL initialize `python-dotenv` and load the appropriate environment file based on the `ENV` variable.

#### Scenario: Load Settings from ENV
- Given `ENV=dev` in `.env`.
- When `settings.py` is loaded.
- Then `.env.dev` is loaded and `DEBUG` is set based on its content.

### Requirement: Dynamic Database Selection
The database backend SHALL switch between PostgreSQL (production/dev) and SQLite (testing) automatically.

#### Scenario: SQLite for Testing
- When running `python manage.py test`.
- Then the `DATABASES` setting uses the SQLite backend.

### Requirement: Conditional Storage
The project SHALL support switching between local file storage and AWS S3 based on the `STORAGE_AWS` environment variable.

#### Scenario: AWS Storage enabled
- Given `STORAGE_AWS=True`.
- When the application handles file uploads.
- Then files are uploaded to the configured S3 bucket.
