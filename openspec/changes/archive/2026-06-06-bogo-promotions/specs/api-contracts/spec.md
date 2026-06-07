## MODIFIED Requirements

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

#### Scenario: Backward compatibility note
- **NOTE** The previous `service_ids` array format is **REMOVED** in favor of the `services` object array format. Clients MUST be updated to send `services` with `service_id` and `quantity` fields.

## ADDED Requirements

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
