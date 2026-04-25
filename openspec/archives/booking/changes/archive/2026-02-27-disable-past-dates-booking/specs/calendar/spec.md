## MODIFIED Requirements

### Requirement: Interactive Date Selection
The component SHALL allow users to select a single date and display its detailed status, restricted to future dates only.

#### Scenario: Prevent Past Date Selection
- **GIVEN** the current date is "Today"
- **WHEN** the calendar is displayed
- **THEN** all dates before and including "Today" MUST be disabled and non-selectable.

#### Scenario: Hide Availability for Past Dates
- **GIVEN** a date that is in the past but marked as "Available" in the data source
- **WHEN** the calendar renders
- **THEN** that date MUST NOT show the green availability accent and MUST be disabled.
