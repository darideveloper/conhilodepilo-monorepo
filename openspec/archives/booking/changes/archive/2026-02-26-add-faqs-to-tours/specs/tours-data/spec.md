# Spec: Tours Data Enhancement (FAQs)

## ADDED Requirements

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
