# Tasks: Refine Admin Sidebar

## Implementation
- [x] Update `project/settings.py` with expanded `UNFOLD["SIDEBAR"]["navigation"]`.
    - [x] Add "Gestión" section with Bookings and Events.
    - [x] Add "Configuración" section with Company Availability and Company Profile.
    - [x] Add Material Icons for each item.
- [x] Verify that all strings are translated using `_()`.

## Validation
- [x] Log in to the admin interface and verify the sidebar structure matches the proposal.
- [x] Click each link to ensure it directs to the correct changelist or singleton change form.
- [x] Verify icons are displayed correctly.
- [x] Check for any console errors or Django warnings related to URL resolution.
