# core-settings Specification Delta

## ADDED Requirements

### Requirement: Default Language Configuration
The project's default language SHALL be configured to Spanish (`es`).

#### Scenario: Spanish Language Setup
- Given the Django application is running.
- When `LANGUAGE_CODE` is loaded from settings.
- Then the language code MUST be `"es"` by default.

#### Scenario: Environment Override for Language
- Given `LANGUAGE_CODE=en-us` in the environment.
- When the Django application starts.
- Then the `LANGUAGE_CODE` setting MUST be `"en-us"`.

### Requirement: Environment Variable Documentation
All environment-specific configuration files (`.env*`) SHALL include the `LANGUAGE_CODE` variable to ensure visibility across different stages.

#### Scenario: Sync Environment Examples
- Given the `.env.example` file.
- When a new language setting is introduced.
- Then `.env.example` MUST be updated with the `LANGUAGE_CODE` variable.