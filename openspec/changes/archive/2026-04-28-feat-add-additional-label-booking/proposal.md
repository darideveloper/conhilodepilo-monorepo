# Proposal: Add "(adicional)" to Service Type Label

In the booking process, when one or more services are already selected, the "Tipo de Servicio" label should be updated to include "(adicional)" to indicate that more services can be added.

## Problem
Users might not be clear that they can add multiple services. Appending "(adicional)" to the category label when services are already selected provides a clear visual cue.

## Proposed Solution
- Add a new translation key `additional` to the `form` section in `translations.ts`.
- Update `BookingServiceSelection.tsx` to conditionally append the translation of `additional` to the service type label if `formData.selectedServices.length > 0`.

## Scope
- `booking` project.
- UI changes in `BookingServiceSelection.tsx`.
- Localization changes in `translations.ts`.
