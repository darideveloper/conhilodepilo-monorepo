# Spec: Calendar UI Refinement

This spec defines the visual and structural refinements for the Booking Calendar.

## ADDED Requirements

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
