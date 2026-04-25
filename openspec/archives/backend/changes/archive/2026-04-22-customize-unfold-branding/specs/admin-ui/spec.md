# admin-ui Specification

## MODIFIED Requirements

### Requirement: Modern Admin Interface
The project SHALL use `django-unfold` to provide a modern, Tailwind-based administrative interface with dynamic branding.

#### Scenario: Access Admin Dashboard
- When a superuser logs into `/admin/`.
- Then the interface uses the Unfold theme with dynamic primary colors.
- And the site title and header MUST match the name configured in `CompanyProfile`.
- And the sidebar logo MUST match the logo configured in `CompanyProfile`.

#### Scenario: Logo and Title Display
- GIVEN `UNFOLD["SITE_LOGO"]` is omitted and `UNFOLD["SITE_ICON"]` is set
- WHEN the admin dashboard renders
- THEN the company logo and the company name MUST display side-by-side in the top-left header.

## ADDED Requirements

### Requirement: Template-based CSS Variable Injection
The admin interface SHALL inject dynamic primary color shades into the document `:root` using a template override.

#### Scenario: Apply Dynamic Colors
- GIVEN the `skeleton.html` override is active
- WHEN the admin dashboard is loaded
- THEN the `--brand-primary-500` CSS variable MUST match the `brand_color` in the `CompanyProfile`.
