# Spec: Calendar Color Refactor

This spec defines the requirements for unifying the Booking Calendar's visual representation with the project's official OKLCH brand theme.

## ADDED Requirements

### Requirement: Theme Consistency
The project SHALL exclusively use the project's brand color palette (Pomegranate Red, Cream, Charcoal) for all availability states, defined using OKLCH values in the global theme.

#### Scenario: Verify OKLCH Theme Synchronization
- Given the `src/styles/global.css` file.
- When inspected.
- Then `--primary` MUST be `oklch(0.577 0.245 27.325)` in the `:root`.
- And it MUST NOT use legacy hex status colors (`#2E7D32` or `#D4A017`).

#### Scenario: Verify Calendar Theme Mapping
- Given the `BookingCalendar` component.
- When rendered.
- Then "Full" status MUST use `destructive` (Brand Red).
- And "Available" status MUST use `primary`.
