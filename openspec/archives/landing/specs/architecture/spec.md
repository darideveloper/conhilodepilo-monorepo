# architecture Specification

## Purpose
TBD - created by archiving change refactor-architecture-tailwind. Update Purpose after archive.
## Requirements
### Requirement: Atomic Design Structure
The project MUST organize components based on the Atomic Design philosophy to categorize reusability scopes.

#### Scenario: Subfolder hierarchy constraints
- **WHEN** adding a new component into the project
- **THEN** it strictly goes into `src/components/atoms`, `src/components/molecules`, or `src/components/organisms`.
- AND an atom contains purely un-opinionated generic components.
- AND molecules combine atoms into moderately complex but still reusable interfaces.
- AND organisms build final large sections relying on atomic primitives.

