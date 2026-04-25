# admin-ui Specification Delta

## ADDED Requirements

### Requirement: Read-Only Service Summary
The service type management interface SHALL show a non-editable summary of associated services.

#### Scenario: Read-only Services within Service Type Admin
- **Given** the `EventType` ModelAdmin.
- **When** viewing the "Services" tab.
- **Then** the list of services MUST be read-only.
- **And** the interface MUST NOT provide a button to add new services from this view.
- **And** the interface MUST NOT allow deleting services from this view.
- **And** each service MUST display its name, price, and duration as non-editable text.
- **And** each row MUST include a link/icon to navigate to the full service details.
