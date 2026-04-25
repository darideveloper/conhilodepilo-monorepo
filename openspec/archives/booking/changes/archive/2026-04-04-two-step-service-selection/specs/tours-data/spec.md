# Spec Delta: Categorized Tour Data

## ADDED Requirements

### Requirement: Categorized Service Data
The application data structure MUST support categorization to enable multi-step selection processes.

#### Scenario: Categorized Data Structure (NEW)
- **GIVEN** the `src/data/booking.json` file
- **WHEN** the application loads
- **THEN** it MUST provide a nested array of "Service Type" (category) objects.
- **AND** each category object MUST have a unique `id` and a `name` (multilingual).
- **AND** each category MUST contain a `services` array with individual service (tour) objects.

#### Scenario: Service Object Structure (MODIFIED)
- **GIVEN** a service object within a category
- **WHEN** the application renders it
- **THEN** it MUST follow the standard service structure (e.g., `id`, `title`, `meta_title`, `meta_description`, `price`, `duration`, `dates`, `faqs`).
- **AND** all services within the categorization MUST use dummy data for testing purposes.