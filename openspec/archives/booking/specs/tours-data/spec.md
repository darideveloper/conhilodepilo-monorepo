# tours-data Specification

## Purpose
TBD - created by archiving change add-faqs-to-tours. Update Purpose after archive.
## Requirements
### Requirement: Include FAQs in Tour Data
Every tour object in the catalog MUST provide a set of frequently asked questions to assist potential visitors.

#### Scenario: Displaying FAQs on Tour Details
- **GIVEN** a tour object from `src/data/tours.json`
- **WHEN** the tour details are rendered
- **THEN** it should have access to a `faqs` property containing an array of at least 2 question-answer pairs.

#### Scenario: Language Consistency
- **GIVEN** the project's primary language is Spanish
- **WHEN** FAQs are added to the data
- **THEN** both `question` and `answer` fields MUST be written in professional Spanish.

#### Scenario: Tour-Specific Content
- **GIVEN** a tour with a specific theme (e.g., "Religioso")
- **WHEN** FAQs are generated
- **THEN** the content MUST reflect that theme and provide relevant historical or logistical context.

### Requirement: Tour Availability Data
Every tour object in the catalog MUST provide accurate availability information for booking using an exclusion-based model.

#### MODIFIED Scenario: Consistency in Availability Patterns
- **GIVEN** a tour object in `src/data/tours.json`
- **WHEN** availability arrays are populated
- **THEN** it MUST prioritize weekends (Saturdays and Sundays) as `limited`.
- **AND** it MUST keep the `booked` array empty for all tours.
- **AND** it MUST NOT include an `available` property, as all future dates are available by default.

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

