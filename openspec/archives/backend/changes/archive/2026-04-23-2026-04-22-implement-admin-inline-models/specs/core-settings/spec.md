# Capability: Core Settings

## ADDED Requirements

### Requirement: Streamlined Sidebar Navigation
The administrative sidebar SHALL focus on high-priority tasks by hiding secondary models that are managed through inlines.

#### Scenario: Optimize Navigation Menu
- **Given** the `UNFOLD["SIDEBAR"]` configuration in `settings.py`.
- **When** inline models are implemented for `Event` and `CompanyProfile`.
- **Then** redundant links to `AvailabilitySlot`, `CompanyAvailability`, etc., must be removed from the sidebar.
- **And** specifically, the "Disponibilidad" item must be removed from the "Configuración" section.
- **And** only the primary entities (`Bookings`, `Services`, `Company Profile`) should remain visible in their respective categories.
