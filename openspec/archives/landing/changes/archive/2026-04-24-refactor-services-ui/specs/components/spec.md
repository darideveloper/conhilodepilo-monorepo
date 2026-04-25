# components Specification

## MODIFIED Requirements

### Requirement: Service Presentation
The system SHALL present services grouped by their respective categories using an interactive card interface that aligns with the brand's visual identity.

#### Scenario: Browsing service categories
- **WHEN** the user views the services section on the homepage
- **THEN** they see a responsive grid of Category Cards.
- AND each card displays the category's image, title, and description.

#### Scenario: Inspecting specific services
- **WHEN** the user interacts with a Category Card
- **THEN** they can select from a list of nested services rendered as interactive pills.
- AND selecting a service dynamically updates the card to display the specific price and duration for that service.
