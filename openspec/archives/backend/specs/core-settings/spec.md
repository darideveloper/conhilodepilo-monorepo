# core-settings Specification

## Purpose
TBD - created by archiving change setup-initial-dashboard. Update Purpose after archive.
## Requirements
### Requirement: Dynamic Settings Initialization
The `settings.py` SHALL initialize `python-dotenv` and load the appropriate environment file based on the `ENV` variable.

#### Scenario: Load Settings from ENV
- Given `ENV=dev` in `.env`.
- When `settings.py` is loaded.
- Then `.env.dev` is loaded and `DEBUG` is set based on its content.

### Requirement: Dynamic Database Selection
The database dashboard SHALL switch between PostgreSQL (production/dev) and SQLite (testing) automatically.

#### Scenario: SQLite for Testing
- When running `python manage.py test`.
- Then the `DATABASES` setting uses the SQLite dashboard.

### Requirement: Conditional Storage
The project SHALL support switching between local file storage and AWS S3 based on the `STORAGE_AWS` environment variable.

#### Scenario: AWS Storage enabled
- Given `STORAGE_AWS=True`.
- When the application handles file uploads.
- Then files are uploaded to the configured S3 bucket.

### Requirement: Branding Context Processor
The project SHALL include a context processor to provide derived brand colors and site identity to all templates.

#### Scenario: Inject Site Identity Globally
- **Given** the `brand_theme_context` context processor is registered.
- **When** any template is rendered.
- **Then** the context variables `site_title` and `site_header` MUST be available and populated from the `CompanyProfile` model via callbacks.

### Requirement: Default Language Configuration
The project's default language SHALL be configured to Spanish (`es`), and it SHALL support local translation overrides using English as the source language for all translatable strings.

#### Scenario: Standardized Localization Identifiers
- **Given** any ModelAdmin, context processor, or settings file.
- **When** defining translatable strings using `_()`.
- **Then** the string inside `_()` MUST be in English.
- **And** the Spanish translation MUST be provided in the corresponding `.po` file.

#### Scenario: Comprehensive UI Localization
- **Given** the Spanish locale is active.
- **When** navigating the admin sidebar, tabs, and fieldsets.
- **Then** all labels MUST appear in Spanish.
- **And** no English fallback labels SHOULD be visible in the primary navigation or configuration areas.

### Requirement: Environment Variable Documentation
All environment-specific configuration files (`.env*`) SHALL include the `LANGUAGE_CODE` variable to ensure visibility across different stages.

#### Scenario: Sync Environment Examples
- Given the `.env.example` file.
- When a new language setting is introduced.
- Then `.env.example` MUST be updated with the `LANGUAGE_CODE` variable.

### Requirement: Streamlined Sidebar Navigation
The administrative sidebar SHALL focus on high-priority tasks by hiding secondary models that are managed through inlines.

#### Scenario: Optimize Navigation Menu
- **Given** the `UNFOLD["SIDEBAR"]` configuration in `settings.py`.
- **When** inline models are implemented for `Event` and `CompanyProfile`.
- **Then** redundant links to `AvailabilitySlot`, `CompanyAvailability`, etc., must be removed from the sidebar.
- **And** specifically, the "Disponibilidad" item must be removed from the "Configuración" section.
- **And** only the primary entities (`Bookings`, `Services`, `Company Profile`) should remain visible in their respective categories.

### Requirement: Global App Translation
Application-level configurations (like `AppConfig`) MUST have translatable labels to support consistent multi-language dashboard interfaces.

#### Scenario: Translating App Labels
- GIVEN the Django Admin
- WHEN viewing the application list in English
- THEN the "booking" app MUST be labeled "Booking Management" (or similar).
- WHEN switching to Spanish
- THEN the "booking" app MUST be labeled "Gestión de Reservas" (or similar).

