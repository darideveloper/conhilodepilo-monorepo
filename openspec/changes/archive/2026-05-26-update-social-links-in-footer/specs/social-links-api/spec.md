## ADDED Requirements

### Requirement: CompanyProfile stores social media URLs
The `CompanyProfile` model SHALL have fields `instagram_url` and `tiktok_url` of type `URLField`, both nullable and optional (blank=True, null=True).

#### Scenario: Admin can set Instagram URL
- **WHEN** an admin edits the CompanyProfile in Django admin and sets the Instagram URL field
- **THEN** the value is persisted in the database

#### Scenario: Admin can set TikTok URL
- **WHEN** an admin edits the CompanyProfile in Django admin and sets the TikTok URL field
- **THEN** the value is persisted in the database

#### Scenario: Social fields are optional
- **WHEN** a new CompanyProfile is created without providing Instagram or TikTok URLs
- **THEN** both fields default to NULL without error

### Requirement: API exposes social media URLs
The `/api/config/` endpoint SHALL include `instagram_url` and `tiktok_url` in its JSON response when they are non-null.

#### Scenario: API returns Instagram URL when set
- **WHEN** the Instagram URL is set on CompanyProfile
- **THEN** `GET /api/config/` returns `{"instagram_url": "https://www.instagram.com/conhilodepilospain", ...}`

#### Scenario: API returns null for unset social URLs
- **WHEN** the Instagram and TikTok URLs are not set on CompanyProfile
- **THEN** `GET /api/config/` returns `{"instagram_url": null, "tiktok_url": null}`

### Requirement: Frontend footer renders social icons
The landing page footer SHALL render clickable Instagram and TikTok icons pointing to the respective URLs. The URLs SHALL be sourced from the API config when available, falling back to hardcoded defaults when the API is unreachable.

#### Scenario: Footer shows Instagram icon with real URL
- **WHEN** the footer renders and `instagram_url` is available from config or fallback
- **THEN** an Instagram icon is rendered as a link to `https://www.instagram.com/conhilodepilospain`

#### Scenario: Footer shows TikTok icon with real URL
- **WHEN** the footer renders and `tiktok_url` is available from config or fallback
- **THEN** a TikTok icon is rendered as a link to `https://www.tiktok.com/@conhilodepilo`

#### Scenario: Social links open in new tab
- **WHEN** a user clicks a social media icon in the footer
- **THEN** the link opens in a new browser tab with `rel="noopener noreferrer"`
