## MODIFIED Requirements

### Requirement: Dashboard Service Categorization
The dashboard system MUST allow grouping service categories (Event Types) into broader groups to facilitate filtering and specialization of the booking flow, and MUST allow administrators to configure per-service BOGO promotions via `buy_x` and `get_y_free` fields on the Event model.

#### Scenario: Assign Group to Event Type
- **Given** an existing `EventType` "Depilación con hilo".
- **And** a group "Salon Services" with ID 1.
- **When** the admin assigns "Salon Services" to "Depilación con hilo".
- **Then** the API MUST return `group_id: 1` for that event type.

#### Scenario: Configure BOGO promotion on a service
- **GIVEN** an existing `Event` "Eyebrow Threading"
- **WHEN** the admin sets `buy_x=2` and `get_y_free=1` on that Event in Django admin
- **THEN** the promotion fields SHALL be persisted and returned via the services API

## ADDED Requirements

### Requirement: Event Promotion Fields
The `Event` model SHALL have `buy_x` (PositiveIntegerField, default=0) and `get_y_free` (PositiveIntegerField, default=0) fields to configure threshold-style BOGO promotions per service.

#### Scenario: Default values on new Event
- **WHEN** a new Event is created without specifying promotion fields
- **THEN** `buy_x` SHALL be 0 and `get_y_free` SHALL be 0

#### Scenario: Active promotion
- **WHEN** an Event has `buy_x > 0` and `get_y_free > 0`
- **THEN** the promotion SHALL be considered active for that service

### Requirement: Booking Price Snapshot Fields
The `Booking` model SHALL have `original_amount`, `discount_amount`, and `total_amount` fields (DecimalField, max_digits=10, decimal_places=2, default=0) to persist the original subtotal, promotional savings, and payable total at booking creation time.

#### Scenario: Booking with discount
- **WHEN** a booking is created with promotional savings
- **THEN** `original_amount`, `discount_amount`, and `total_amount` SHALL be stored with the calculated values

#### Scenario: Booking without discount
- **WHEN** a booking is created with no promotions applicable
- **THEN** `discount_amount` SHALL default to 0.00
- **AND** `original_amount` SHALL equal `total_amount`

### Requirement: BookingServiceThrough Custom M2M Model
The `Booking.services` ManyToManyField SHALL use a custom through model `BookingServiceThrough` with `quantity` (PositiveIntegerField, default=1) and `unit_price` (DecimalField, max_digits=10, decimal_places=2) to represent how many of each service are included in a booking and the service price at booking time.

#### Scenario: Creating a booking with quantities
- **WHEN** a booking is created with Service A (quantity=3) and Service B (quantity=1)
- **THEN** two `BookingServiceThrough` rows SHALL be created: one with `quantity=3` and booking-time `unit_price` for Service A, and one with `quantity=1` and booking-time `unit_price` for Service B

#### Scenario: Existing data migration
- **WHEN** the through model migration runs
- **THEN** all existing `booking_booking_services` rows SHALL be migrated to `BookingServiceThrough` with `quantity=1` and `unit_price` copied from each Event's current price

#### Scenario: Unique constraint
- **WHEN** creating a BookingServiceThrough row
- **THEN** the combination of `(booking_id, event_id)` SHALL be unique — a booking cannot have two rows for the same service

#### Scenario: Explicit related names
- **WHEN** code accesses a Booking's service line items
- **THEN** it SHALL use the `booking_services` related name from `BookingServiceThrough.booking`
