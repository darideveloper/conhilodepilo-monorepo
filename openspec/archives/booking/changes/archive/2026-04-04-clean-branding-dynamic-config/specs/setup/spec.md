# Capability: Setup and External Integration

This capability handles the initial setup of the project and its integration with external systems.

## ADDED Requirements

### Requirement: Removal of Deprecated External Scripts
The deprecated scripts and styles for external integration MUST be removed.

#### Scenario: No WordPress Integration
- **GIVEN** the codebase.
- **WHEN** inspecting the `src/assets/` directory.
- **THEN** the `wordpress/` subdirectory and its contents MUST NOT exist.
