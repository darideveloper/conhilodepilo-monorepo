# Spec: Spanish Language Standard

## Purpose
This spec defines the language requirements for the project's user interface to ensure a consistent Spanish-first experience for visitors interested in Granada's culture and history.
## Requirements
### Requirement: Spanish-First UI
The project's user interface SHALL be developed primarily in Spanish to align with the local context of Granada and its target audience.

#### Scenario: Verify Visible Text
- **GIVEN** a user-visible component.
- **WHEN** rendered.
- **THEN** all labels, buttons, and instructional text MUST be in Spanish.

### Requirement: Calendar Localization
Interactive date pickers and calendars SHALL use the Spanish locale for time-related labels.

#### Scenario: Verify Calendar Locale
- **GIVEN** the `BookingCalendar` component.
- **WHEN** rendered.
- **THEN** month names (e.g., "Enero") and day abbreviations (e.g., "L", "M") MUST be in Spanish.

### Requirement: Multi-language Support (Overridable)
The application SHALL support multiple languages, but specific UI labels provided by the dynamic configuration MUST take precedence over static translation file values.

#### Scenario: Verify Label Override
- **GIVEN** the static Spanish translation for `calendar.tourLabel` is "Tour".
- **AND** the dynamic configuration has `event_type_label: "Experiencia"`.
- **WHEN** the `useTranslation` hook is used.
- **THEN** it MUST return "Experiencia" instead of "Tour".

#### Scenario: Fallback to Static Defaults
- **GIVEN** the dynamic configuration is not yet loaded OR specific label fields (e.g., `event_type_label`) are missing.
- **WHEN** the `useTranslation` hook is used.
- **THEN** it MUST fall back to the values defined in the `translations.ts` file for the current language.

#### Scenario: Availability Status Label Mapping
- **GIVEN** a configuration object with specific availability labels.
- **WHEN** the availability statuses are rendered in the calendar or legend.
- **THEN** the mapping MUST be:
    - `availability_free_label` -> `status.available`
    - `availability_regular_label` -> `status.standard`
    - `availability_no_free_label` -> `status.booked`

