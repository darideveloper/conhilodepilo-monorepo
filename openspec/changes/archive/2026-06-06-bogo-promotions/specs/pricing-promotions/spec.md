# pricing-promotions Specification

## Purpose
Defines the "Buy X Get Y Free" (BOGO) threshold pricing model for services, enabling administrators to configure volume promotions per service and ensuring the system correctly calculates discounts, persists them, and surfaces them to the end user.

## ADDED Requirements

### Requirement: Per-Service BOGO Promotion Configuration
The system SHALL allow administrators to configure a "Buy X Get Y Free" promotion on each `Event` (service) via the Django admin panel.

#### Scenario: Setting a promotion on a service
- **WHEN** an administrator sets `buy_x=2` and `get_y_free=1` on an Event
- **THEN** the system SHALL store these values and treat the service as having an active promotion

#### Scenario: Disabling a promotion
- **WHEN** an administrator sets `buy_x=0` or `get_y_free=0` on an Event
- **THEN** no promotion SHALL apply for that service, regardless of quantity

#### Scenario: Promotion fields are optional with safe defaults
- **WHEN** a new Event is created without specifying promotion fields
- **THEN** `buy_x` SHALL default to `0` and `get_y_free` SHALL default to `0`, meaning no promotion is active

### Requirement: Threshold-Style Discount Calculation
The system SHALL calculate free items using threshold-style logic: for every `buy_x` quantity purchased, `get_y_free` items are free, with thresholds stacking.

#### Scenario: Buy 2 Get 1 Free with quantity 2
- **GIVEN** a service with `buy_x=2` and `get_y_free=1` priced at €30
- **WHEN** a user books quantity 2
- **THEN** 1 threshold is met, 1 item is free, the discount is €30, and the payable amount is €30

#### Scenario: Buy 2 Get 1 Free with quantity 4
- **GIVEN** a service with `buy_x=2` and `get_y_free=1` priced at €30
- **WHEN** a user books quantity 4
- **THEN** 2 thresholds are met, 2 items are free, the discount is €60, and the payable amount is €60

#### Scenario: Buy 2 Get 1 Free with quantity 3
- **GIVEN** a service with `buy_x=2` and `get_y_free=1` priced at €30
- **WHEN** a user books quantity 3
- **THEN** 1 threshold is met, 1 item is free, the discount is €30, and the payable amount is €60

#### Scenario: Buy 2 Get 1 Free with quantity 1
- **GIVEN** a service with `buy_x=2` and `get_y_free=1` priced at €30
- **WHEN** a user books quantity 1
- **THEN** no threshold is met, no discount applies, and the payable amount is €30

#### Scenario: No promotion configured
- **GIVEN** a service with `buy_x=0` and `get_y_free=0` priced at €30
- **WHEN** a user books any quantity
- **THEN** no discount applies and the total is `quantity × €30`

### Requirement: Price Snapshot Persistence on Booking
The system SHALL persist pricing snapshots on each Booking and BookingServiceThrough record so that historical pricing remains accurate even if service prices or promotions change later.

#### Scenario: Booking with discount
- **WHEN** a booking is created with services that have an active promotion
- **THEN** the system SHALL store `original_amount`, `discount_amount`, and `total_amount` on the Booking record
- **AND** each BookingServiceThrough row SHALL store the service `unit_price` used at booking creation time

#### Scenario: Booking without discount
- **WHEN** a booking is created with no promotions applicable
- **THEN** `discount_amount` SHALL default to `0.00`
- **AND** `original_amount` SHALL equal `total_amount`

#### Scenario: Service price changes after booking
- **GIVEN** a booking was created when Service A cost €30
- **AND** Service A later changes to €40
- **WHEN** the booking is viewed in admin or synced to Google Calendar
- **THEN** the booking SHALL continue to show the original €30 unit price and stored booking totals

### Requirement: Duration Unaffected by Promotion
The system SHALL calculate booking duration based on the total quantity of all services, without any discount reduction.

#### Scenario: Duration includes free items
- **GIVEN** a service with `duration_minutes=30` and a "Buy 2 Get 1 Free" promotion
- **WHEN** a user books quantity 3
- **THEN** the total appointment duration SHALL be 90 minutes (3 × 30), even though only 2 are charged

### Requirement: Custom Through Model for Service Quantities
The system SHALL use a custom M2M through model `BookingServiceThrough` with `quantity` and `unit_price` fields to represent how many of each service are in a booking and the unit price charged at booking time, replacing the default auto-generated through table.

#### Scenario: Booking with quantity > 1 for a service
- **WHEN** a user books Service A with quantity 3
- **THEN** the `BookingServiceThrough` table SHALL contain a single row with `booking_id`, `event_id`, `quantity=3`, and the booking-time `unit_price`
- **AND** the booking's total duration SHALL be `3 × ServiceA.duration_minutes`
- **AND** the booking's total price before discount SHALL be `3 × ServiceA.price`

#### Scenario: Booking with multiple services
- **WHEN** a user books Service A × 2 and Service B × 1
- **THEN** the `BookingServiceThrough` table SHALL contain two rows: `(booking_id, eventA_id, quantity=2)` and `(booking_id, eventB_id, quantity=1)`

#### Scenario: Existing bookings migrated with quantity=1
- **WHEN** the through model migration runs on existing data
- **THEN** all existing M2M rows SHALL be migrated to `BookingServiceThrough` with `quantity=1` and `unit_price` copied from the current Event price

### Requirement: Frontend Quantity Selection
The booking frontend SHALL allow users to select multiple quantities of the same service.

#### Scenario: Adding quantity to a service
- **WHEN** a user selects a service that already exists in their cart
- **THEN** the quantity SHALL increment rather than being rejected as a duplicate

#### Scenario: Adjusting quantity
- **WHEN** a user increases or decreases the quantity via +/- controls
- **THEN** the cart SHALL update the quantity and recalculate the subtotal and discount

#### Scenario: Minimum quantity
- **WHEN** a user tries to reduce the quantity below 1
- **THEN** the service SHALL be removed from the cart entirely

### Requirement: Frontend Price Breakdown Display
The booking frontend SHALL display a price summary showing the original subtotal, any promotional discount, and the final total.

#### Scenario: Booking with promotion
- **GIVEN** a cart with "Eyebrow Threading" × 3 at €30 each with Buy 2 Get 1 Free
- **WHEN** the user views the booking summary
- **THEN** the UI SHALL display:
  - Subtotal: 3 × €30 = €90
  - Promotion: -€30 (Buy 2 Get 1 Free)
  - Total: €60

#### Scenario: Booking without promotion
- **GIVEN** a cart with services that have no promotions
- **WHEN** the user views the booking summary
- **THEN** the UI SHALL display only the total (or subtotal equal to total with no discount line)

### Requirement: Promotion Badge on Service Selection
The service selection UI SHALL display a visible "Buy X Get Y Free" badge next to any service that has an active promotion.

#### Scenario: Service with active promotion
- **GIVEN** a service with `buy_x=2` and `get_y_free=1`
- **WHEN** the service appears in the selection dropdown or cart
- **THEN** the UI SHALL display a badge or label reading "Buy 2 Get 1 Free" (localized)

#### Scenario: Service without promotion
- **GIVEN** a service with `buy_x=0`
- **WHEN** the service appears in the selection dropdown or cart
- **THEN** no promotion badge SHALL be displayed

### Requirement: Multi-Service Cart Discount Aggregation
When a cart contains multiple distinct services with different promotions, the system SHALL calculate each service's discount independently and sum them for the total discount.

#### Scenario: Two services with different promotions
- **GIVEN** Service A with Buy 2 Get 1 Free (€30) at quantity 3, and Service B with no promotion (€50) at quantity 1
- **WHEN** the booking is submitted
- **THEN** the total discount SHALL be €30 (from Service A only) and the total payable SHALL be €80 (€60 + €50)

### Requirement: Quantity-Aware Availability
The availability engine SHALL compute time-slot availability using quantity-adjusted durations, so that booking the same service multiple times reserves the correct total time.

#### Scenario: Availability for service with quantity > 1
- **GIVEN** Service A with `duration_minutes=30` selected at quantity 3
- **WHEN** available time slots are fetched
- **THEN** the engine SHALL compute `total_duration = 3 × 30 = 90` minutes and only return slots with at least 90 minutes of free time
