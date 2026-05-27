## MODIFIED Requirements

### Requirement: Header navigation links MUST use absolute paths
The main navigation links and primary call-to-action (CTA) buttons in the Header component MUST use absolute root paths (e.g., `/#section-id`) rather than relative hash links (e.g., `#section-id`) to ensure they function correctly from any subpage. The navigation SHALL NOT include a "Sobre mí" link in the header.

#### Scenario: Navigating from a subpage
- **WHEN** a user is on a subpage
- **AND** they click a navigation link or the "Reserva Ahora" CTA button in the Header
- **THEN** they are correctly redirected to the homepage and scrolled to the respective section (e.g., `/#servicios`, `/#cursos`, `/#resultados`, or `/#footer`)

#### Scenario: Header does not include "Sobre mí" link
- **WHEN** the Header component renders its navigation links
- **THEN** the "Sobre mí" link (`/#info`) SHALL NOT appear in the navigation