# api-contracts Specification

## Purpose
Defines the API contracts for the booking platform, including booking creation, availability queries, and service listings. This delta adds gift-related fields to the create booking endpoint.

## ADDED Requirements

### Requirement: Create Booking Endpoint accepts gift fields
The `POST /api/bookings/` endpoint SHALL accept the following optional gift-related fields in the request payload:
- `isGift` (boolean, default false)
- `buyerName` (string, required when isGift=true, otherwise defaults to clientName)
- `buyerEmail` (string, required when isGift=true, otherwise defaults to clientEmail)
- `recipientName` (string, required when isGift=true)
- `recipientEmail` (string, required when isGift=true)

The `clientName` and `clientEmail` fields remain required and SHALL always represent the final service recipient.

#### Scenario: Successful gift booking creation
- **WHEN** a valid JSON payload is submitted with `isGift: true`, `clientName: "Bob"`, `clientEmail: "bob@test.com"`, `buyerName: "Alice"`, `buyerEmail: "alice@test.com"`, `recipientName: "Bob"`, `recipientEmail: "bob@test.com"` along with standard booking fields
- **THEN** the API MUST create a booking with `is_gift=True`, `buyer_name="Alice"`, `buyer_email="alice@test.com"`, `client_name="Bob"`, `client_email="bob@test.com"`
- **AND** return a success response with `booking_id` and standard fields

#### Scenario: Successful non-gift booking creation (backward compatible)
- **WHEN** a valid JSON payload is submitted without any gift fields (existing clients)
- **THEN** the API MUST create a booking with `is_gift=False`, `buyer_name=client_name`, `buyer_email=client_email`
- **AND** the response SHALL be identical to the pre-gift response format

#### Scenario: Gift booking rejected without recipient fields
- **WHEN** a payload is submitted with `isGift: true` but missing `recipientName` or `recipientEmail`
- **THEN** the API MUST reject the request with HTTP 400

#### Scenario: Gift booking with partial gift data
- **WHEN** a payload is submitted with `isGift: true` but `recipientName` present and `recipientEmail` missing
- **THEN** the API MUST reject the request with HTTP 400

### Requirement: Booking response includes gift fields
The create booking response SHALL include `is_gift`, `buyer_name`, `buyer_email` in the response payload when a gift booking is created.

#### Scenario: Gift booking response
- **WHEN** a gift booking is successfully created
- **THEN** the response SHALL include `is_gift: true`, `buyer_name: "Alice"`, `buyer_email: "alice@test.com"`
