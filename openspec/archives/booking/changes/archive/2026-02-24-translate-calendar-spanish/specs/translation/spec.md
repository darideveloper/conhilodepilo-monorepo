# Spec: Spanish Language Standard

This spec defines the language requirements for the project's user interface.

## ADDED Requirements

### Requirement: Spanish-First UI
The project's user interface SHALL be developed primarily in Spanish to align with the local context of Granada and its target audience.

#### Scenario: Verify Visible Text
- Given a user-visible component.
- When rendered.
- Then all labels, buttons, and instructional text MUST be in Spanish.

### Requirement: Calendar Localization
Interactive date pickers and calendars SHALL use the Spanish locale for time-related labels.

#### Scenario: Verify Calendar Locale
- Given the `BookingCalendar` component.
- When rendered.
- Then month names (e.g., "Enero") and day abbreviations (e.g., "L", "M") MUST be in Spanish.
