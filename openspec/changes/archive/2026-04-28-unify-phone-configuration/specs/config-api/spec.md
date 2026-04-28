# spec.md

## ADDED Requirements

### Requirement: Global Configuration Fetching
The system MUST provide a way to fetch the global company configuration from the backend API.

#### Scenario: Fetch configuration from API
1.  **Given** the backend API is available at `/api/config/`.
2.  **When** the `getConfig` utility is called.
3.  **Then** it should return an object containing `contact_phone`, `contact_email`, and other branding details.

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
