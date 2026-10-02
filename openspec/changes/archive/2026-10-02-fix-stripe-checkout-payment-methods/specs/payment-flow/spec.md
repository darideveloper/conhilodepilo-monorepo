## ADDED Requirements

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
