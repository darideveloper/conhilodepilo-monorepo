# Spec: Architectural and Structural Refactoring

## Purpose
This spec defines the requirements for architectural improvements and structural refactoring within the project, ensuring maintainability, consistency, and a clean separation of concerns.

## Requirements

### Requirement: Theme Consistency
The project SHALL exclusively use the project's brand color palette (Pomegranate Red, Cream, Charcoal) for all availability states, defined using OKLCH values in the global theme.

#### Scenario: Verify OKLCH Theme Synchronization
- **GIVEN** the `src/styles/global.css` file.
- **WHEN** inspected.
- **THEN** `--primary` MUST be `oklch(0.577 0.245 27.325)` in the `:root`.
- **AND** it MUST NOT use legacy hex status colors (`#2E7D32` or `#D4A017`).

#### Scenario: Verify Calendar Theme Mapping
- **GIVEN** the `BookingCalendar` component.
- **WHEN** rendered.
- **THEN** "Full" status MUST use `destructive` (Brand Red).
- **AND** "Available" status MUST use `primary`.

### Requirement: Configuration-Driven Status Rendering
The component SHALL use a centralized configuration object to determine the visual properties (icons, colors, labels) of all availability states.

#### Scenario: Visual Consistency
- **GIVEN** a `STATUS_CONFIG` object.
- **WHEN** a status changes.
- **THEN** all UI elements (icons, colors, badges) MUST update according to the configuration without hardcoded logic in the main render loop.

### Requirement: Component Modularity
The `BookingCalendar` SHALL be decomposed into sub-components for the Legend and Selected Date Details to improve separation of concerns.

#### Scenario: Sub-component Verification
- **GIVEN** the `BookingCalendar` file.
- **WHEN** inspected.
- **THEN** it MUST contain distinct components for `StatusLegend` and `StatusDetails` (or equivalent names).

### Requirement: Data Normalization
The `bookingData` structure SHALL align with the unified status keys used in the configuration object.

#### Scenario: Mapping Consistency
- **GIVEN** a `bookingData` object.
- **WHEN** compared to `STATUS_CONFIG` keys.
- **THEN** the property names MUST match the status keys (`booked`, `limited`, `available`).
