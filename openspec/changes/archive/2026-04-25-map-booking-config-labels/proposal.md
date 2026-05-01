# Map Booking Config Labels

## Summary
Updates the `booking` application frontend to accurately map configuration API responses to internal i18n labels. Currently, "Pocas plazas" is incorrectly mapped to `standard` instead of `limited`, and `extras_label` from the API is completely ignored. This proposal corrects these bindings so the UI displays the correct text from the dashboard configuration.

## Scope
- Correct the mapping of `availability_regular_label` to the `limited` status.
- Add the mapping of `extras_label` to the `form.specialRequests` and `stripe.requests` translations in `useTranslation.ts`.

## Context
The booking app consumes an API config endpoint. While some labels like `company_name` and `availability_free_label` work, the regular availability (Pocas plazas) and the special requests form field do not respect the config response because of mapping errors and omissions in the frontend code.

## Architecture
No structural changes. Just a bug fix/enhancement to the existing React i18n mapping logic in `useTranslation.ts`.