# Spec Delta: Booking UI Service Type Label

## ADDED Requirements

### Requirement: Show "adicional" in Service Type label when services are selected
The "Tipo de Servicio" (or configured label) in the first step of the booking form MUST include "(adicional)" if at least one service has already been added to the selection.

#### Scenario: No services selected
- GIVEN the user is on Step 1 of the booking form
- AND no services have been added to the selection yet
- THEN the service type label should be "Tipo de Servicio" (or its configured/translated value)

#### Scenario: At least one service selected
- GIVEN the user is on Step 1 of the booking form
- AND at least one service has been added to `formData.selectedServices`
- THEN the service type label should be "Tipo de Servicio (adicional)" (or its configured/translated value followed by "(adicional)")
