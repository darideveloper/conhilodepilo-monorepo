# config-api Specification

## Purpose
The `config-api` specification defines the central configuration management for the system, including company profile data, contact information, social media links, and branding details, exposed via a central API for consumption across all platform services.

## Requirements
### Requirement: Global Configuration Fetching
The system MUST provide a way to fetch the global company configuration from the dashboard API, and the services API MUST include promotion fields for each service.

#### Scenario: Fetch configuration from API
1.  **Given** the dashboard API is available at `/api/config/`.
2.  **When** the `getConfig` utility is called.
3.  **Then** it should return an object containing `contact_phone`, `contact_email`, and other branding details.

### Requirement: Services API Exposes Promotion Fields
The `/api/services/` endpoint SHALL include `buy_x` and `get_y_free` fields in each service object so the frontend can display promotion badges and calculate discounts.

#### Scenario: Service with active promotion
- **WHEN** a service has `buy_x=2` and `get_y_free=1`
- **THEN** the API response for that service SHALL include `buy_x: 2` and `get_y_free: 1`

#### Scenario: Service without promotion
- **WHEN** a service has `buy_x=0` and `get_y_free=0`
- **THEN** the API response SHALL include `buy_x: 0` and `get_y_free: 0`

### Requirement: Availability Endpoints Accept Quantities
The `/api/availability/days/` and `/api/availability/slots/` endpoints SHALL accept an optional `quantities` query parameter (comma-separated integers) parallel to `service_ids`, representing the quantity of each service. When provided, total duration SHALL be computed as `SUM(duration × quantity)` instead of `SUM(duration)`.

#### Scenario: Availability with quantities
- **WHEN** `GET /api/availability/days/?service_ids=1,2&quantities=3,1` is requested
- **AND** Service 1 has `duration_minutes=30` and Service 2 has `duration_minutes=60`
- **THEN** the total duration SHALL be `3×30 + 1×60 = 150` minutes
- **AND** only days with at least 150 minutes of available time SHALL be returned

#### Scenario: Availability without quantities (backward compatible)
- **WHEN** `GET /api/availability/days/?service_ids=1,2` is requested (no `quantities` parameter)
- **THEN** all quantities SHALL default to 1 (existing behavior preserved)

#### Scenario: Availability quantity count mismatch
- **WHEN** `GET /api/availability/days/?service_ids=1,2&quantities=3` is requested
- **THEN** the endpoint SHALL return HTTP 400

#### Scenario: Availability invalid quantity
- **WHEN** `GET /api/availability/slots/?service_ids=1&quantities=0&date=2026-06-10` is requested
- **THEN** the endpoint SHALL return HTTP 400 because quantity must be a positive integer

### Requirement: Phone Formatting
The system MUST correctly format phone numbers for both display and programmatic use (WhatsApp links).

#### Scenario: Format phone for WhatsApp
1.  **Given** a phone number with special characters like `+34 915-23-14-06`.
2.  **When** the WhatsApp formatter is used.
3.  **Then** it should return `34915231406` (digits only).

#### Scenario: Format phone for Display
1.  **Given** a raw phone number `915231406`.
2.  **When** the display formatter is used.
3.  **Then** it should return a human-readable format like `915 23 14 06`.

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

