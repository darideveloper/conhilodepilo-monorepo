# ui-refinement Specification

## Purpose
TBD - created by archiving change refine-calendar-ui. Update Purpose after archive.
## Requirements
### Requirement: Interactive Hover State
The calendar's date cells SHALL use the project's `brand-charcoal` color for their background on hover for a high-contrast and brand-consistent feel.

#### Scenario: Verify Calendar Day Hover
- Given the `BookingCalendar` component.
- When a user hovers over a date cell.
- Then the background MUST change to `brand-charcoal` and the text MUST change to `white`.

### Requirement: Responsive Visibility
The Booking Calendar SHALL be visible and accessible on all screen sizes, adapting its positioning and width accordingly.

#### Scenario: Mobile Display
- Given a screen width less than `1024px` (mobile/tablet).
- When the home page is loaded.
- Then the `BookingCalendar` MUST be visible and SHOULD use the maximum available width (with reasonable padding).

#### Scenario: Desktop Display
- Given a screen width of `1024px` or greater (desktop).
- When the home page is loaded.
- Then the `BookingCalendar` MUST be visible and SHOULD use fixed positioning (e.g., top-right).

### Requirement: Header Cleanup
The Booking Calendar component SHALL NOT display the redundant "Booking Schedule" title or description.

#### Scenario: Verify Title Removal
- Given the `BookingCalendar` component.
- When rendered.
- Then the "Booking Schedule" title and description MUST NOT be present.

### Requirement: Brand-Integrated Scroll Bar
The application SHALL provide a custom scroll bar design that is visually integrated with the application's brand identity.

#### Scenario: Apply Brand-Colored Scroll Bar
- **GIVEN** the application has loaded its dynamic brand configuration.
- **AND** the `--brand-color` CSS variable is set.
- **WHEN** the user interacts with a scrollable area.
- **THEN** the scroll bar thumb and track MUST reflect the brand-consistent styling, using the `--brand-color` variable to ensure cohesion.

