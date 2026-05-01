## RENAMED Requirements
- FROM: `### Requirement: Single Host Setting`
- TO: `### Requirement: Single Dashboard Host Setting`
- FROM: `### Requirement: Removal of Redundant SITE_URL`
- TO: `### Requirement: Removal of Redundant Dashboard SITE_URL`
- FROM: `### Requirement: Automatic ALLOWED_HOSTS Inclusion`
- TO: `### Requirement: Automatic Dashboard ALLOWED_HOSTS Inclusion`

## MODIFIED Requirements
### Requirement: Single Dashboard Host Setting
The dashboard service SHALL use a single `HOST` environment variable to define its base URL.

#### Scenario: Media URL Generation
- **GIVEN** `HOST` is set to `http://localhost:8000`
- **WHEN** a media URL is generated for a local file `/media/test.jpg`
- **THEN** the returned URL SHALL be `http://localhost:8000/media/test.jpg`

#### Scenario: Stripe Redirect URLs
- **GIVEN** `HOST` is set to `https://api.example.com`
- **WHEN** a Stripe checkout session is created
- **THEN** the `success_url` and `cancel_url` SHALL be prefixed with `https://api.example.com` (or the configured fallback)

### Requirement: Removal of Redundant Dashboard SITE_URL
The dashboard service SHALL NOT rely on a `SITE_URL` environment variable.

#### Scenario: Environment Validation
- **GIVEN** a `.env` file containing both `HOST` and `SITE_URL`
- **WHEN** the dashboard starts
- **THEN** it SHALL only use the `HOST` value for its base URL configuration

### Requirement: Automatic Dashboard ALLOWED_HOSTS Inclusion
The dashboard service SHALL automatically include the hostname derived from the `HOST` variable in the `ALLOWED_HOSTS` list.

#### Scenario: Hostname Extraction
- **GIVEN** `HOST` is set to `https://dashboard.example.com`
- **AND** `ALLOWED_HOSTS` is empty
- **WHEN** the settings are loaded
- **THEN** `ALLOWED_HOSTS` SHALL contain `dashboard.example.com`
