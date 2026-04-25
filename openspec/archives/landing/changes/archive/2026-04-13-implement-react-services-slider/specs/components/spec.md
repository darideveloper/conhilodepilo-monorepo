# Components Specification (Delta)

## ADDED Requirements

### Requirement: Service Presentation
The system MUST support a scalable React-based slider for services that includes category filtering.

#### Scenario: `ServicesSlider` displays and filters services
- **GIVEN** a list of services with categories
- **WHEN** rendered in the `ServicesSlider` component
- **THEN** it displays filter buttons for each unique category, plus an "All" option
- **AND** it renders a Swiper slider containing only the services matching the selected category