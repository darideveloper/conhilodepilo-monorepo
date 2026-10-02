# payment-flow Specification

## Purpose
TBD - created by archiving change implement-stripe-checkout. Update Purpose after archive.
## Requirements
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

### Requirement: Landing Page Fulfillment
The Landing App SHALL provide success and cancellation landing pages to handle the user's return from Stripe, ensuring a full-page experience.

#### Scenario: Return from Stripe Success
- **GIVEN** a user successfully completes a Stripe payment
- **WHEN** they are redirected back to the Landing App `/success` page
- **THEN** the page SHALL display a confirmation message
- **AND** the user SHALL be outside the booking iframe

#### Scenario: Return from Stripe Cancel
- **GIVEN** a user cancels or backs out of a Stripe payment
- **WHEN** they are redirected back to the Landing App `/cancel` page
- **THEN** the page SHALL display a message indicating the payment was not completed
- **AND** the page SHALL provide a way to return to the booking section

### Requirement: Abandoned PRE-PAID Booking Cleanup
The dashboard SHALL release time slots held by `PENDING` bookings whose Stripe Checkout Session has expired, so that abandoned checkouts do not block other users indefinitely.

#### Scenario: Stale PENDING Booking Older Than TTL
- **GIVEN** a `Booking` with `status='PENDING'` and `created_at` older than `STRIPE_PENDING_BOOKING_TTL_HOURS` (default 24)
- **WHEN** the `cleanup_abandoned_bookings` management command runs
- **THEN** the booking SHALL be deleted
- **AND** the time slot SHALL become available to other users on the next availability query

#### Scenario: Recent PENDING Booking Within TTL
- **GIVEN** a `Booking` with `status='PENDING'` and `created_at` within the TTL window
- **WHEN** the cleanup command runs
- **THEN** the booking SHALL NOT be modified

#### Scenario: Non-PENDING Bookings Are Never Cleaned
- **GIVEN** a `Booking` with `status` of `CONFIRMED`, `PAID`, or `CANCELLED`
- **WHEN** the cleanup command runs, regardless of `created_at`
- **THEN** the booking SHALL NOT be modified

#### Scenario: Dry Run
- **GIVEN** the cleanup command is invoked with `--dry-run`
- **WHEN** matching stale bookings exist
- **THEN** the command SHALL log the booking IDs that would be deleted
- **AND** SHALL NOT mutate the database

### Requirement: Multi-Tenant Stripe Product Naming
The Stripe Checkout Session line-item name SHALL be derived from the configured `CompanyProfile.name`, not a hard-coded brand string, so the dashboard remains white-label correct. The line-item SHALL reflect the discounted total.

#### Scenario: Company Profile Has A Name
- **GIVEN** `CompanyProfile.get_solo().name` returns `"Acme Spa"`
- **WHEN** a Stripe Checkout Session is created
- **THEN** the line-item `product_data.name` SHALL contain `"Acme Spa"` (exact format may include a "Reserva — " prefix or equivalent)

#### Scenario: Company Profile Name Is Blank
- **GIVEN** `CompanyProfile.get_solo().name` is empty or `None`
- **WHEN** a Stripe Checkout Session is created
- **THEN** the line-item `product_data.name` SHALL fall back to a generic, non-brand-specific string (e.g. `"Booking"`)

#### Scenario: Payment amount reflects discount
- **GIVEN** a booking with a promotional discount of €30
- **WHEN** a Stripe Checkout Session is created
- **THEN** the `unit_amount` SHALL be the discounted total, not the original subtotal

#### Scenario: Payment amount uses booking snapshot
- **GIVEN** a booking was created with stored `total_amount=60.00`
- **WHEN** a Stripe Checkout Session is created
- **THEN** the `unit_amount` SHALL be derived from the stored `total_amount`

### Requirement: Dynamic Payment Methods
Stripe Checkout Sessions SHALL be created without the deprecated `payment_method_types` parameter, which the current Stripe API rejects for Checkout Sessions. The payment methods offered to the customer SHALL be managed by the Stripe Dashboard's dynamic payment methods configuration, not hard-coded in the dashboard. The Stripe Python SDK SHALL be pinned to a tested version so that image rebuilds cannot silently pull a breaking major.

#### Scenario: Checkout Session created without payment_method_types
- **GIVEN** a booking with at least one `PRE-PAID` service and a positive total
- **WHEN** the Stripe Checkout Session is created
- **THEN** the request SHALL NOT include the `payment_method_types` parameter
- **AND** the session SHALL be created successfully (no `InvalidRequestError`)

#### Scenario: Payment methods come from the Dashboard
- **GIVEN** Card is enabled in the Stripe Dashboard payment methods settings
- **WHEN** a customer is redirected to the Checkout Session
- **THEN** Card SHALL be offered, along with any other payment method enabled in the Dashboard

#### Scenario: Stripe SDK pinned to a tested version
- **GIVEN** the dashboard dependency manifest
- **WHEN** the container image is rebuilt
- **THEN** the installed Stripe SDK version SHALL be exactly `16.0.0`

