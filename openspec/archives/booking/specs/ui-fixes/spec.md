# ui-fixes Specification

## Purpose
TBD - created by archiving change fix-booking-form-bugs. Update Purpose after archive.
## Requirements
### Requirement: Calendar Initial State
The `BookingCalendar` SHALL be initialized to a neutral state with no date pre-selected on initial load.

#### Scenario: Verify Initial Selection
- **GIVEN** the `BookingCalendar` component.
- **WHEN** the page is loaded.
- **THEN** no date MUST be selected.
- **AND** the `StatusDetails` section MUST NOT be visible.

### Requirement: Selected Date Styling
The selected date in the `Calendar` component SHALL be visually distinct and consistent with the project's brand identity.

#### Scenario: Verify Selected Date Color
- **GIVEN** a date in the `Calendar` component.
- **WHEN** selected by the user.
- **THEN** the date's background MUST be `bg-foreground` (black/charcoal).
- **AND** the date's text MUST be `text-background` (cream/white).

