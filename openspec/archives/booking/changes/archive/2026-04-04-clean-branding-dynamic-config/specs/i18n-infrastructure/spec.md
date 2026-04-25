# Capability: i18n Infrastructure

This capability handles internationalization, including translations and dynamic text based on user preferences and API configuration.

## ADDED Requirements

### Requirement: Dynamic Translation Titles
The application MUST use dynamic company names in translated titles instead of hardcoded branding.

#### Scenario: Use API Company Name in Title
- **GIVEN** a config from `/api/config/` containing `company_name`.
- **WHEN** generating page titles or headers.
- **THEN** the application MUST use `company_name` instead of hardcoded "Granada Go Tours".
