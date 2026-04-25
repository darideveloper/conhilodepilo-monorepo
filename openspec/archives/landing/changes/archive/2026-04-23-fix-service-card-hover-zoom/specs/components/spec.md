# components Specification Delta

## MODIFIED Requirements

### Requirement: Service Presentation
The system MUST support a scalable React-based slider for services that includes category filtering.

#### Scenario: `ServiceCard` and `CourseCard` hover zoom is isolated
- **GIVEN** a `ServiceCard` or `CourseCard`
- **WHEN** the user hovers over a specific card
- **THEN** only the image within that specific card MUST scale
- **AND** hovering over a parent container with a `group` class MUST NOT trigger the zoom effect for all nested cards
