# Capability: Admin UI

## ADDED Requirements

### Requirement: Modern Admin Interface
The project SHALL use `django-unfold` to provide a modern, Tailwind-based administrative interface.

#### Scenario: Access Admin Dashboard
- When a superuser logs into `/admin/`.
- Then the interface uses the Unfold theme with custom primary colors and the site title is "Con Hilo Depilo".
- And the sidebar navigation includes "Usuarios" and "Grupos".

### Requirement: Markdown Support in Admin
Text areas in the admin interface SHALL support Markdown editing via SimpleMDE.

#### Scenario: Edit Markdown Field
- When editing a model with a text area in the admin.
- Then the field is enhanced with a SimpleMDE editor.

### Requirement: Environment Badges
The admin interface SHALL display a badge indicating the current environment (Production, Development, etc.).

#### Scenario: Display Environment Badge
- Given `ENV=prod`.
- When accessing the admin.
- Then a "Production" badge is visible in the header.
