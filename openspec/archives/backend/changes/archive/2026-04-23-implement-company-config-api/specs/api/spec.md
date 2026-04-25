# API Specification

## Purpose
Define the public API surface for the booking system, starting with company configuration.

## Requirements

## ADDED Requirements

### Requirement: Company Configuration Endpoint
The system SHALL provide a public GET endpoint at `/api/config/` that returns the current company's branding, contact information, and UI labels.

#### Scenario: Fetch Configuration Successfully
- GIVEN a `CompanyProfile` with name "My Business" and brand color `#ee5837`.
- WHEN a `GET` request is made to `/api/config/`.
- THEN the response status MUST be `200 OK`.
- AND the JSON body MUST contain:
    - `company_name`: "My Business"
    - `brand_color`: "#ee5837"
    - `timezone`: The configured system timezone.
    - `currency`: "EUR" (or current config).
    - `event_type_label`: Current configured label.

#### Scenario: Handle Missing Logo
- GIVEN a `CompanyProfile` with no logo uploaded.
- WHEN a `GET` request is made to `/api/config/`.
- THEN the `logo` field in the response MUST be `null`.

#### Scenario: Public Access
- GIVEN an unauthenticated user.
- WHEN a `GET` request is made to `/api/config/`.
- THEN the response status MUST be `200 OK`.
