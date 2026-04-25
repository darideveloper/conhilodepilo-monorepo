# Spec Delta: Admin UI Title Consistency

## ADDED Requirements

### Requirement: Dynamic Admin Page Titles
The admin interface MUST consistently display the company name in the HTML `<title>` tag across all pages, incorporating specific page titles when available.

#### Scenario: Navigating to a Change List
- GIVEN a user is logged into the admin dashboard
- WHEN they navigate to the "Reservas" changelist
- THEN the browser tab title MUST show "Seleccione Reserva a cambiar | [Company Name]"
- AND the HTML `<title>` tag MUST NOT be empty.

#### Scenario: Fallback Site Title
- GIVEN an admin page that does not explicitly set a page-specific title
- WHEN the page is rendered
- THEN the browser tab title MUST show at least the site title from `CompanyProfile`.
