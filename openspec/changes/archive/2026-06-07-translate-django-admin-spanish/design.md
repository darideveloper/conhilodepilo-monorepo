## Context

The Spanish localization catalog for the Django admin dashboard ([django.po](file:///develop/monorepos/conhilorepilo/dashboard/locale/es/LC_MESSAGES/django.po)) currently contains multiple missing translations (empty `msgstr`) and fuzzy matches (`#, fuzzy`) for key model fields and admin UI components. This document outlines the approach to filling and compiling these translations.

## Goals / Non-Goals

**Goals:**
- Provide complete Spanish translations for all Booking, Event, and Integration admin fields.
- Clean up fuzzy markers so that Django uses the correct translated labels instead of fallback English strings.
- Compile the updated `.po` catalog into a binary `.mo` file ready for production.

**Non-Goals:**
- Modifying the Python source files or changing any field definitions.
- Translating third-party packages (like Unfold admin search) unless they are customizable within project settings.

## Decisions

### Decision: Direct modification of `django.po` and manual compile
We will edit the existing `django.po` file directly and use Django's standard translation compilation tool to build the `.mo` file.
* **Alternative considered**: Running `python manage.py makemessages` first. However, since we already have the source file with the exact empty/fuzzy entries identified, modifying it directly avoids risks of unintended string resets.
* **Reasoning**: It is cleaner and directly solves the issue.

## Risks / Trade-offs

- **Risk**: Compiling messages requires the `gettext` binary installed on the system.
  - *Mitigation*: Ensure `gettext` is installed or compile within the environment where development tools are active.
