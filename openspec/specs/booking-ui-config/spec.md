# booking-ui-config Specification

## Purpose
TBD - created by archiving change map-booking-config-labels. Update Purpose after archive.
## Requirements
### Requirement: Map limited availability label
The Booking UI SHALL map the API configuration field `availability_regular_label` to the `status.limited` internal i18n key instead of `status.standard`.

#### Scenario: Displaying "Pocas plazas" label
- Given the backend API returns `"availability_regular_label": "Poca disponibilidad"`.
- When the `StatusLegend` or `BookingCalendar` components render the limited status.
- Then the frontend SHALL display "Poca disponibilidad" for the limited status text instead of the default "Pocas plazas".

### Requirement: Map extras form label
The Booking UI SHALL map the API configuration field `extras_label` to the `form.specialRequests` and `stripe.requests` internal i18n keys.

#### Scenario: Displaying special requests field label
- Given the backend API returns `"extras_label": "Extras"`.
- When the Booking form renders the special requests field.
- Then the field label SHALL display "Extras (opcional)" instead of "Peticiones especiales (opcional)".

