# courses Specification

## Purpose
TBD - created by archiving change add-courses. Update Purpose after archive.
## Requirements
### Requirement: Courses Display
The system SHALL provide a showcase section for Academy Courses, displaying the duration, title, description, and a representative optimized image.

#### Scenario: Displaying multiple courses
- **WHEN** the user visits the homepage
- **THEN** they are presented with a grid of available courses

#### Scenario: Course details
- **WHEN** observing a single course card
- **THEN** the duration is displayed dynamically based on the numeric minutes provided by the dashboard (e.g., formatted to hours or days).
- AND the description is parsed from markdown to standard HTML.

