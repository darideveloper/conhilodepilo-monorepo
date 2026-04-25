# translation Spec Delta

## ADDED Requirements

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
