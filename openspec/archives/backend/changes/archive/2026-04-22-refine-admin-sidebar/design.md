# Design: Admin Sidebar Reorganization

## Context
The project uses `django-unfold`, which provides a customizable sidebar via the `UNFOLD["SIDEBAR"]["navigation"]` setting. Currently, this is hardcoded with only the "Autenticación" group.

## Architectural Reasoning
- **Grouping by Domain:** Models are grouped by their operational role rather than their Django app structure. 
    - **Gestión:** Operational data that changes frequently (Bookings) and the catalog (Events).
    - **Configuración:** Static or semi-static settings that define how the business operates (Availability, Profile).
- **Material Icons:** We will use standard Google Material Icons (available in Unfold) to provide visual cues for each navigation item.
- **Lazy Evaluation:** Using `reverse_lazy` ensures that URL resolution happens at the right time in the Django lifecycle, preventing circular import issues or early resolution errors.

## Components
- **Settings Update:** Modify `project/settings.py` to expand the `UNFOLD` configuration.
- **Translation Keys:** Ensure all strings are wrapped in `_()` (gettext_lazy).

## Trade-offs
- **Maintenance:** Adding hardcoded links to the sidebar means that if models are renamed or moved between apps, the `settings.py` file must be updated. This is a standard trade-off for highly customized admin interfaces in Django.
