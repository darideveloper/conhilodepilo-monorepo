# Spec: Atomic Design Component Structure

## Purpose
This spec mandates the use of Atomic Design principles for organizing UI components to ensure scalability, reusability, and clear architectural separation of concerns within the project.

## Requirements

### Requirement: Atomic Hierarchy
All components SHALL be organized into one of three tiers: Atoms, Molecules, or Organisms.

#### Scenario: Verify Component Location
- **GIVEN** a component file.
- **WHEN** categorized.
- **THEN** it MUST reside in the corresponding sub-directory:
    - Basic primitives (buttons, badges, inputs) -> `atoms/`.
    - Simple groups of atoms (legends, details) -> `molecules/`.
    - Complex, stateful, or logic-heavy sections -> `organisms/`.

### Requirement: Directory Structure
The `src/components` directory SHALL follow a specific folder structure.

#### Scenario: Verify Folder Layout
- **GIVEN** the `src/components` directory.
- **WHEN** inspected.
- **THEN** it MUST contain `atoms/`, `molecules/`, and `organisms/` folders.

### Requirement: Import Consistency
Import paths SHALL correctly reflect the atomic structure.

#### Scenario: Verify Import Path
- **GIVEN** a file importing a component.
- **WHEN** inspected.
- **THEN** the import path MUST include the atomic tier (e.g., `@/components/atoms/...`).
