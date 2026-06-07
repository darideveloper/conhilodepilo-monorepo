# dashboard-models Specification

## Purpose
TBD - created by archiving change group-services-by-type. Update Purpose after archive.
## Requirements
### Requirement: Privacy Policy Configuration
The system MUST allow an administrator to configure a privacy policy URL for the company.

#### Scenario: Fetching company profile
- **WHEN** the company configuration is requested
- **THEN** the configuration MUST include a valid `privacy_policy_url`.

### Requirement: Terms and Conditions Configuration
The system MUST allow an administrator to configure a Terms and Conditions URL for the company.

#### Scenario: Fetching company profile
- **WHEN** the company configuration is requested
- **THEN** the configuration MUST include a valid `terms_and_conditions_url`.

### Requirement: Booking Special Requests Storage
The system MUST store any special requests made by the user during the booking process.

#### Scenario: Persisting a booking
- **WHEN** a user provides special requests in the contact form
- **THEN** the system MUST save them in the corresponding booking record.

### Requirement: Global Booking Cooldown
The system MUST allow an administrator to define a global "cool down" period (in minutes) that is enforced between consecutive bookings.

#### Scenario: Configuring cooldown
- **WHEN** the administrator updates the Company Profile with a `booking_cooldown_minutes` value of `15`.
- **THEN** all subsequent availability calculations MUST ensure at least a 15-minute gap exists between the end of one booking and the start of the next.

### Requirement: Dashboard Service Categorization
The dashboard system MUST allow grouping service categories (Event Types) into broader groups to facilitate filtering and specialization of the booking flow. The `Event` model no longer carries per-service promotion fields — promotion configuration is now global via `CompanyProfile`.

#### Scenario: Assign Group to Event Type
- **Given** an existing `EventType` "Depilación con hilo".
- **And** a group "Salon Services" with ID 1.
- **When** the admin assigns "Salon Services" to "Depilación con hilo".
- **Then** the API MUST return `group_id: 1` for that event type.

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

### Requirement: CompanyProfile Promotion Fields
The `CompanyProfile` singleton model SHALL have `buy_x` (PositiveIntegerField, default=0) and `get_y_free` (PositiveIntegerField, default=0) fields to configure a global threshold-style BOGO promotion applied to all services.

#### Scenario: Default values
- **WHEN** a new CompanyProfile is created without specifying promotion fields
- **THEN** `buy_x` SHALL be 0 and `get_y_free` SHALL be 0 (promotion disabled)

#### Scenario: Promotion active globally
- **WHEN** `CompanyProfile.buy_x > 0` and `CompanyProfile.get_y_free > 0`
- **THEN** the promotion SHALL be considered active for ALL services

### Requirement: Gift fields on Booking model
The `Booking` model SHALL have the following additional fields to support gift bookings:

- `is_gift`: `BooleanField(default=False)` — whether this booking is a gift
- `buyer_name`: `CharField(max_length=255)` — the name of the person who submitted the form (always filled)
- `buyer_email`: `EmailField()` — the email of the person who submitted the form (always filled)
- `recipient_name`: `CharField(max_length=255, blank=True, null=True)` — the gift recipient name (null when not a gift)
- `recipient_email`: `EmailField(blank=True, null=True)` — the gift recipient email (null when not a gift)

The existing `client_name` and `client_email` fields SHALL continue to represent the final service recipient:
- When `is_gift=False`: `client_name=buyer_name`, `client_email=buyer_email`
- When `is_gift=True`: `client_name=recipient_name`, `client_email=recipient_email`

#### Scenario: New gift booking stored correctly
- **WHEN** a gift booking is created with buyer name "Alice" and recipient name "Bob"
- **THEN** `is_gift` SHALL be `True`
- **AND** `buyer_name` SHALL be "Alice"
- **AND** `client_name` SHALL be "Bob" (the recipient)
- **AND** `recipient_name` SHALL be "Bob"

#### Scenario: New non-gift booking stored correctly
- **WHEN** a non-gift booking is created with buyer name "Alice"
- **THEN** `is_gift` SHALL be `False`
- **AND** `buyer_name` SHALL be "Alice"
- **AND** `client_name` SHALL be "Alice"
- **AND** `recipient_name` SHALL be `None`

### Requirement: Migration populates buyer fields for existing records
A data migration SHALL set `is_gift=False`, `buyer_name=client_name`, and `buyer_email=client_email` for all existing Booking records where these fields are null.

#### Scenario: Existing booking migration
- **WHEN** the migration runs against an existing booking with `client_name="Alice"`, `client_email="alice@test.com"`
- **THEN** the booking SHALL have `is_gift=False`, `buyer_name="Alice"`, `buyer_email="alice@test.com"`

