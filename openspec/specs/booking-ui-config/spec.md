# booking-ui-config Specification

## Purpose
TBD - created by archiving change map-booking-config-labels. Update Purpose after archive.
## Requirements
### Requirement: Map limited availability label
The Booking UI SHALL map the API configuration field `availability_regular_label` to the `status.limited` internal i18n key instead of `status.standard`.

#### Scenario: Displaying "Pocas plazas" label
- Given the dashboard API returns `"availability_regular_label": "Poca disponibilidad"`.
- When the `StatusLegend` or `BookingCalendar` components render the limited status.
- Then the frontend SHALL display "Poca disponibilidad" for the limited status text instead of the default "Pocas plazas".

### Requirement: Map extras form label
The Booking UI SHALL map the API configuration field `extras_label` to the `form.specialRequests` and `stripe.requests` internal i18n keys.

#### Scenario: Displaying special requests field label
- Given the dashboard API returns `"extras_label": "Extras"`.
- When the Booking form renders the special requests field.
- Then the field label SHALL display "Extras (opcional)" instead of "Peticiones especiales (opcional)".

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

