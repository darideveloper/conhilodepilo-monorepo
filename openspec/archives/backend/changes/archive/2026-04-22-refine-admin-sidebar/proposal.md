# Proposal: Refine Admin Sidebar for Business Operations

## Summary
Update the Django admin sidebar (Unfold theme) to prioritize models that are critical for business operations and configuration. This change will reorganize the navigation to provide a more intuitive experience for the business owner, grouping models into logical sections like "Gestión" (Operations) and "Configuración" (Setup).

## Problem Statement
The current admin sidebar only displays standard "Authentication" (Users and Groups) and hides all other models under the default "All Applications" view (which is currently disabled). This makes it difficult for a business owner to quickly access core functionalities like Bookings, Services, and Availability settings.

## Proposed Changes
1.  **Reorganize Sidebar:** Implement a structured navigation in `UNFOLD["SIDEBAR"]["navigation"]` within `settings.py`.
2.  **Add "Gestión" Section:** Include direct links to "Bookings" (Reservas) and "Events" (Servicios).
3.  **Add "Configuración" Section:** Include direct links to "Company Availability" (Disponibilidad) and "Company Profile" (Perfil de Empresa).
4.  **Internationalization:** Use `gettext_lazy` for all sidebar titles and labels to support localization.

## Impact
- **Improved UX:** Faster access to the most used modules for the business owner.
- **Clarity:** Clearer separation between system administration (Users/Groups) and business logic (Bookings/Services).
- **Consistency:** Aligns the admin interface with the "Con Hilo Depilo" branding and operational needs.
