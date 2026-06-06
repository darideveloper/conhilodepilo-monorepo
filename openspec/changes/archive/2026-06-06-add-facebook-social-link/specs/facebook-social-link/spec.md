## ADDED Requirements

### Requirement: CompanyProfile stores Facebook URL
The `CompanyProfile` model SHALL have a `facebook_url` field of type `URLField`, nullable and optional (blank=True, null=True).

#### Scenario: Admin can set Facebook URL
- **WHEN** an admin edits the CompanyProfile in Django admin and sets the Facebook URL field
- **THEN** the value is persisted in the database

#### Scenario: Facebook field is optional
- **WHEN** a new CompanyProfile is created without providing a Facebook URL
- **THEN** the field defaults to NULL without error

### Requirement: API exposes Facebook URL
The `/api/config/` endpoint SHALL include `facebook_url` in its JSON response when non-null.

#### Scenario: API returns Facebook URL when set
- **WHEN** the Facebook URL is set on CompanyProfile
- **THEN** `GET /api/config/` returns `{"facebook_url": "https://www.facebook.com/conhilodepilo", ...}`

#### Scenario: API returns null for unset Facebook URL
- **WHEN** the Facebook URL is not set on CompanyProfile
- **THEN** `GET /api/config/` returns `{"facebook_url": null}`

### Requirement: Frontend footer renders Facebook icon
The landing page footer SHALL render a clickable Facebook icon pointing to the Facebook URL. The URL SHALL be sourced from the API config when available, falling back to a hardcoded default (`"#"`) when the API is unreachable. The icon SHALL be placed between Instagram and TikTok in the social links row.

#### Scenario: Footer shows Facebook icon with placeholder URL
- **WHEN** the footer renders and `facebook_url` is not configured
- **THEN** a Facebook icon is rendered as a link to `"#"`

#### Scenario: Footer shows Facebook icon with admin-set URL
- **WHEN** the footer renders and `facebook_url` is set via admin
- **THEN** a Facebook icon is rendered as a link to the configured URL

#### Scenario: Facebook link opens in new tab
- **WHEN** a user clicks the Facebook icon in the footer
- **THEN** the link opens in a new browser tab with `rel="noopener noreferrer"`
