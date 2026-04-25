# Spec: i18n Infrastructure

## ADDED Requirements

### Requirement: Multi-Language UI Support
The project's user interface SHALL support multiple languages, starting with Spanish (ES) as the default and English (EN) as a secondary option.

#### Scenario: Default Language is Spanish
- **GIVEN** the application is loaded for the first time.
- **WHEN** checked.
- **THEN** the language MUST be Spanish ('es').

#### Scenario: Change Language to English
- **GIVEN** the language is Spanish ('es').
- **WHEN** the user selects English through the language toggle.
- **THEN** all UI labels and tour data MUST switch to English.

#### Scenario: Language Persistence
- **GIVEN** the user has selected English.
- **WHEN** the page is reloaded.
- **THEN** the language MUST still be English.

### Requirement: Bilingual Tour Data
The tour data source (`tours.json`) SHALL provide information in both Spanish and English for all customer-facing fields.

#### Scenario: Render Tour in English
- **GIVEN** the current language is English.
- **AND** a tour is selected.
- **WHEN** rendered.
- **THEN** its title, introduction, and descriptions MUST be in English.

### Requirement: Dynamic Date Localization
Calendars and date formatting SHALL adapt their locale to the currently selected language.

#### Scenario: English Date Formatting
- **GIVEN** the language is English.
- **WHEN** a date is displayed (e.g., in `StatusDetails`).
- **THEN** it MUST use English month names and formatting (e.g., "March 1st, 2026").
