# landing-ui-components Specification

## ADDED Requirements

### Requirement: Header navigation links MUST use absolute paths
The main navigation links in the Header component MUST use absolute root paths (e.g., `/#section-id`) rather than relative hash links (e.g., `#section-id`) to ensure they function correctly from any subpage.

#### Scenario: Navigating from a subpage
- **Given** a user is on a subpage (e.g., a specific tour page)
- **When** they click a navigation link in the Header
- **Then** they are correctly redirected to the homepage and scrolled to the respective section.