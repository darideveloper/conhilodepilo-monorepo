## ADDED Requirements

### Requirement: Admin root redirects to booking changelist

The admin root URL `/admin/` SHALL permanently redirect to `/admin/booking/booking/` (the booking changelist).

#### Scenario: Visiting /admin/ redirects to booking list

- **WHEN** a user visits `/admin/`
- **THEN** they are redirected with a 301 status to `/admin/booking/booking/`

#### Scenario: Other admin URLs are unaffected

- **WHEN** a user visits `/admin/booking/event/`
- **THEN** the request is handled normally by Django admin (no redirect)

#### Scenario: Direct booking URL still works

- **WHEN** a user visits `/admin/booking/booking/` directly
- **THEN** the booking changelist page is rendered normally (no redirect loop)
