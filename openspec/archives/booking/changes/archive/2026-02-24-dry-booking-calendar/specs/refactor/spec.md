# Spec: DRY BookingCalendar Refactor

This spec defines the requirements for refactoring the BookingCalendar to eliminate redundancy.

## ADDED Requirements

### Requirement: Configuration-Driven Status Rendering
The component SHALL use a centralized configuration object to determine the visual properties (icons, colors, labels) of all availability states.

#### Scenario: Visual Consistency
- Given a `STATUS_CONFIG` object.
- When a status changes.
- Then all UI elements (icons, colors, badges) MUST update according to the configuration without hardcoded logic in the main render loop.

### Requirement: Component Modularity
The `BookingCalendar` SHALL be decomposed into sub-components for the Legend and Selected Date Details to improve separation of concerns.

#### Scenario: Sub-component Verification
- Given the `BookingCalendar` file.
- When inspected.
- Then it MUST contain distinct components for `StatusLegend` and `StatusDetails` (or equivalent names).

### Requirement: Data Normalization
The `bookingData` structure SHALL align with the unified status keys used in the configuration object.

#### Scenario: Mapping Consistency
- Given a `bookingData` object.
- When compared to `STATUS_CONFIG` keys.
- Then the property names MUST match the status keys (`booked`, `limited`, `available`).
