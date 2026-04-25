# admin-ui Specification

## MODIFIED Requirements

### Requirement: Modern Admin Interface
The project SHALL use `django-unfold` to provide a modern, Tailwind-based administrative interface with a functional sticky action bar.

#### Scenario: Branding Visibility on Subpages
- GIVEN the superuser is on a model list view (e.g., Bookings) or a change form.
- WHEN the page is rendered.
- THEN the sidebar MUST display the brand logo and site name.
- AND the `branding` template block MUST be explicitly defined in `base_site.html`.

### Requirement: Template-based CSS Variable Injection
The admin interface SHALL inject dynamic primary color shades into the document `:root` using a template override.

#### Scenario: Apply Dynamic Colors without Recursion
- GIVEN the `skeleton.html` override is active.
- WHEN the admin dashboard is loaded.
- THEN the template MUST NOT cause a recursion error during extension.
- AND the `--brand-primary-500` CSS variable MUST match the value provided by the `brand_theme_context`.
