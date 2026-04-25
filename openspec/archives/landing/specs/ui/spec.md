# ui Specification

## Purpose
TBD - created by archiving change 2026-04-24-fix-markdown-bullets. Update Purpose after archive.
## Requirements
### Requirement: Markdown lists must render with bullets and proper padding
- Markdown content rendered in the UI SHALL display bullet points and MUST have padding aligned with the rest of the content.

#### Scenario: User visits a service detail page with markdown description
- GIVEN the service description contains a list (`- item`)
- WHEN the page is rendered
- THEN the markdown list should show bullet points and proper padding aligned with other UI elements.

### Requirement: Global Custom Scrollbar
The application SHALL display a branded custom scrollbar on all overflow-y/overflow-x containers.

#### Scenario: View application in desktop browser
When the content exceeds the viewport height, a branded scrollbar MUST appear using primary brand colors and project radius variables.

