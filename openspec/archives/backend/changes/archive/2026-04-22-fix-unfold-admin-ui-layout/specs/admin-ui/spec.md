# Spec Delta: Admin UI Layout Fix

## MODIFIED Requirements

### Requirement: Modern Admin Interface
The project SHALL use `django-unfold` to provide a modern, Tailwind-based administrative interface with a functional sticky action bar.

#### Scenario: Sticky Bottom Bar Presence
- Given the superuser is on a model change form (e.g., editing a Booking).
- When the page content exceeds the viewport height.
- Then the action bar (containing Save and Delete buttons) SHALL remain pinned to the bottom of the viewport.
- And the layout SHALL use Unfold's standard container classes to ensure proper spacing.

#### Scenario: Standardized Admin UI Features
- Given an admin class inheriting from `ModelAdminUnfoldBase`.
- When accessing the change form.
- Then "Warn Unsaved Changes" MUST be enabled.
- And fields SHALL be displayed in their compressed format by default.
- And a "Cancel" button SHALL be visible in the action bar.
