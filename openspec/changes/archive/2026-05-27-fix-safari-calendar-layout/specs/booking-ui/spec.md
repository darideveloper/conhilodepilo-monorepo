## ADDED Requirements

### Requirement: Safari Layout Compatibility
The booking UI MUST ensure that all interactive elements, including the calendar, are correctly rendered on macOS Safari.

#### Scenario: Calendar Layout Stability
- **WHEN** the calendar month container is rendered
- **THEN** it SHALL explicitly enforce `display: grid` or equivalent layout to prevent Safari rendering bugs.
