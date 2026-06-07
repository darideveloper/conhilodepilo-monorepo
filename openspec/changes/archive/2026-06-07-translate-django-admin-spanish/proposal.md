## Why

The Django admin interface has several untranslated or improperly translated (fuzzy) strings, including key fields on the booking reservation form (such as `Original amount`, `Is gift`, `Google sync status`, etc.). Fully translating these strings to Spanish is necessary to provide a consistent and professional localized experience for Spanish-speaking administrators.

## What Changes

- Update the Spanish translation catalog (`django.po` and compiled `django.mo`) to define Spanish translations for all missing, empty, or fuzzy entries.
- Ensure all key fields and labels on the Booking admin details view (including gift fields, pricing fields, and Google Calendar sync fields) are rendered in Spanish.
- Clean up fuzzy flags in the `.po` catalog so Django correctly loads the defined translations instead of falling back to English.

## Capabilities

### New Capabilities
- None

### Modified Capabilities
- None

## Impact

- **Affected files**: `dashboard/locale/es/LC_MESSAGES/django.po` (and the compiled binary `django.mo`).
- **Dependencies**: No new external dependencies.
- **Affected systems**: Django admin interface forms and lists, specifically the Booking model views.
