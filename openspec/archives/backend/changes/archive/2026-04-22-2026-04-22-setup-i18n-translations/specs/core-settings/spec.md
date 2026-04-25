# Spec Delta: Local Translation Configuration

## MODIFIED Requirements

### Requirement: Default Language Configuration
The project's default language SHALL be configured to Spanish (`es`), and it SHALL support local translation overrides.

#### Scenario: Spanish Language Setup
- Given the Django application is running.
- When `LANGUAGE_CODE` is loaded from settings.
- Then the language code MUST be `"es"` by default.

#### Scenario: Environment Override for Language
- Given `LANGUAGE_CODE=en-us` in the environment.
- When the Django application starts.
- Then the `LANGUAGE_CODE` setting MUST be `"en-us"`.

#### Scenario: Local Translation Support
- Given a `locale/` directory exists in the project root.
- When the Django application starts.
- Then the `LOCALE_PATHS` setting MUST include the path to this directory.
- AND the `LANGUAGES` setting MUST be explicitly defined (e.g., including `es` and `en`).
- AND strings defined in `locale/es/LC_MESSAGES/django.po` MUST take precedence over default translations.
