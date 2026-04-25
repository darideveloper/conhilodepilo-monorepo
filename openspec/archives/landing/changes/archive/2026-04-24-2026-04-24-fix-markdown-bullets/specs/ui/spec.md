## ADDED Requirements

### Requirement: Markdown lists must render with bullets and proper padding
- Markdown content rendered in the UI SHALL display bullet points and MUST have padding aligned with the rest of the content.

#### Scenario: User visits a service detail page with markdown description
- GIVEN the service description contains a list (`- item`)
- WHEN the page is rendered
- THEN the markdown list should show bullet points and proper padding aligned with other UI elements.
