# api-contracts Specification

## Purpose
Defines the API contracts for the booking platform, including booking creation, availability queries, and service listings.

## Requirements
### Requirement: Create Booking Endpoint
The system MUST provide an API endpoint to create a new booking record, accepting a services array with quantity information instead of flat service IDs. The endpoint SHALL create `BookingServiceThrough` rows with the specified quantities and booking-time unit prices.

#### Scenario: Successful booking creation with quantities
- **WHEN** a valid JSON payload containing `services: [{service_id: 1, quantity: 3}, {service_id: 2, quantity: 1}]` along with user details and date/time is submitted
- **THEN** the API MUST create a booking record with `BookingServiceThrough` rows reflecting the specified quantities
- **AND** each through row MUST store `unit_price` from the Event price at booking time
- **AND** the API MUST calculate `discount_amount` based on any applicable promotions using the threshold formula
- **AND** the API MUST calculate `end_time` using quantity-adjusted duration `SUM(service.duration_minutes × quantity)`
- **AND** the API MUST store `original_amount`, `discount_amount`, and `total_amount` on the Booking record
- **AND** the API MUST return a success response with the booking details including `original_amount`, `discount_amount`, and `total_amount`

#### Scenario: Successful booking creation without promotions
- **WHEN** a booking is submitted with services that have no active promotions
- **THEN** the API MUST return `discount_amount: 0.00`
- **AND** `original_amount` MUST equal `total_amount`

#### Scenario: Invalid service quantity
- **WHEN** a booking is submitted with a service quantity of 0 or a negative number
- **THEN** the API MUST reject the request with HTTP 400

### Requirement: Availability Endpoints Accept Quantities
The `/api/availability/days/` and `/api/availability/slots/` endpoints SHALL accept an optional `quantities` query parameter (comma-separated integers) parallel to `service_ids` to support quantity-weighted duration calculation.

#### Scenario: Availability with quantities
- **WHEN** `GET /api/availability/days/?service_ids=1,2&quantities=3,1` is requested
- **THEN** the endpoint SHALL compute `total_duration = SUM(service.duration_minutes × quantity)` and use it for slot fitting

#### Scenario: Availability without quantities
- **WHEN** `GET /api/availability/days/?service_ids=1,2` is requested without `quantities`
- **THEN** all quantities SHALL default to 1 (backward compatible)

#### Scenario: Availability quantities length mismatch
- **WHEN** `GET /api/availability/slots/?service_ids=1,2&quantities=3&date=2026-06-10` is requested
- **THEN** the endpoint SHALL reject the request with HTTP 400

#### Scenario: Availability invalid quantity value
- **WHEN** `GET /api/availability/slots/?service_ids=1&quantities=-1&date=2026-06-10` is requested
- **THEN** the endpoint SHALL reject the request with HTTP 400

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

