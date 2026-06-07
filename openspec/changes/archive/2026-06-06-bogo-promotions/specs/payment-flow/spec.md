## MODIFIED Requirements

### Requirement: Conditional Payment Redirection
The system SHALL determine if a booking requires immediate payment based on the selected services, calculate any applicable discounts, persist booking-time prices, and redirect the user accordingly. Discount calculation SHALL use the `BookingServiceThrough` model's `quantity` and `unit_price` fields to compute per-service and total discounts.

#### Scenario: All services are POST-PAID
- **GIVEN** a user selects only services with `payment_model="POST-PAID"`
- **WHEN** the booking is submitted
- **THEN** the dashboard SHALL set the booking status to `CONFIRMED`
- **AND** the API SHALL return `payment_required: false`
- **AND** the frontend SHALL display the local success message

#### Scenario: At least one service is PRE-PAID
- **GIVEN** a user selects at least one service with `payment_model="PRE-PAID"`
- **WHEN** the booking is submitted
- **THEN** the dashboard SHALL set the booking status to `PENDING`
- **AND** the dashboard SHALL create a Stripe Checkout Session with the **discounted** total amount
- **AND** the API SHALL return `payment_required: true` and a `checkout_url`
- **AND** the frontend SHALL redirect the user to the `checkout_url`

#### Scenario: Booking with promotional discount and PRE-PAID service
- **GIVEN** a user books Service A (PRE-PAID, €30) × 3 with Buy 2 Get 1 Free
- **WHEN** the Stripe Checkout Session is created
- **THEN** the total amount sent to Stripe SHALL be €60 (not €90)

#### Scenario: PRE-PAID booking discounted to zero
- **GIVEN** a user books PRE-PAID services whose promotional discount reduces the booking total to €0
- **WHEN** the booking is submitted
- **THEN** the dashboard SHALL NOT create a Stripe Checkout Session
- **AND** the booking SHALL be completed internally without external payment
- **AND** the API SHALL return `payment_required: false`

### Requirement: Multi-Tenant Stripe Product Naming
The Stripe Checkout Session line-item name SHALL be derived from the configured `CompanyProfile.name`, not a hard-coded brand string, so the dashboard remains white-label correct. The line-item SHALL reflect the discounted total.

#### Scenario: Company Profile Has A Name
- **GIVEN** `CompanyProfile.get_solo().name` returns `"Acme Spa"`
- **WHEN** a Stripe Checkout Session is created
- **THEN** the line-item `product_data.name` SHALL contain `"Acme Spa"` (exact format may include a "Reserva — " prefix or equivalent)

#### Scenario: Payment amount reflects discount
- **GIVEN** a booking with a promotional discount of €30
- **WHEN** a Stripe Checkout Session is created
- **THEN** the `unit_amount` SHALL be the discounted total, not the original subtotal

#### Scenario: Payment amount uses booking snapshot
- **GIVEN** a booking was created with stored `total_amount=60.00`
- **WHEN** a Stripe Checkout Session is created
- **THEN** the `unit_amount` SHALL be derived from the stored `total_amount`
