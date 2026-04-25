# api-service-layer Specification

## Purpose
The API Service Layer defines the requirements for centralized network communication, ensuring consistent multi-tenancy handling, standardized request/response patterns, and robust error management across the system.

## ADDED Requirements
### Requirement: Centralized Multi-Tenant Request Client
The system SHALL provide a centralized API client that identifies the tenant/client based on the request configuration and prepends the client ID to the subdomain.

#### Scenario: Verify Multi-Tenant URL Construction
- **GIVEN** a request with `client: "my-tenant"` and endpoint `config/`.
- **AND** a base API URL like `https://api.example.com/api/`.
- **WHEN** the request is initiated.
- **THEN** the request MUST be sent to `https://my-tenant.api.example.com/api/config/`.

### Requirement: Standardized Configuration Retrieval
The system SHALL provide a dedicated service to fetch tenant-specific configuration during application initialization.

#### Scenario: Successful Fetch of Config
- **GIVEN** a valid client identifier.
- **WHEN** the `fetchConfig` service is called.
- **THEN** it MUST return a configuration object containing `brand_color`, `logo`, `company_name`, and metadata labels.

### Requirement: Standardized Booking Submission
The system SHALL provide a dedicated service to submit booking details to the backend API.

#### Scenario: Successful Booking Submission
- **GIVEN** a completed booking form payload.
- **WHEN** the `submitBooking` service is called.
- **THEN** it MUST send a `POST` request to the configured booking endpoint.
- **AND** it MUST return a Stripe redirect URL on success.
