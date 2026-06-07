## MODIFIED Requirements

### Requirement: Time Slot Selection
The system MUST allow users to select an available time slot after choosing a valid day, and MUST support selecting multiple quantities of the same service with a quantity control interface.

#### Scenario: Displaying available times
- **WHEN** a valid day is selected in the booking calendar
- **THEN** the UI MUST present a list of available time slots and require the user to pick one before proceeding to the contact form.

#### Scenario: Increasing quantity of a selected service
- **WHEN** a user clicks the "+" control on a service already in the cart
- **THEN** the quantity for that service SHALL increment by 1

#### Scenario: Decreasing quantity of a selected service
- **WHEN** a user clicks the "−" control on a service with quantity > 1
- **THEN** the quantity for that service SHALL decrement by 1

#### Scenario: Removing a service from the cart
- **WHEN** a user clicks the "−" control on a service with quantity = 1
- **THEN** the service SHALL be removed from the cart entirely

## ADDED Requirements

### Requirement: Service Quantity in Cart State
The booking store's `selectedServices` array SHALL track quantity per service, with each entry containing `{serviceTypeId, serviceId, quantity}`.

#### Scenario: Adding a service for the first time
- **WHEN** a user adds a service to the cart
- **THEN** the entry SHALL be created with `quantity: 1`

#### Scenario: Adding the same service again
- **WHEN** a user adds a service that already exists in the cart
- **THEN** the existing entry's `quantity` SHALL increment by 1 instead of creating a duplicate

### Requirement: Price Summary in Booking Form
The booking form (Step 3) SHALL display a price breakdown section showing the subtotal, any promotions applied, and the total amount.

#### Scenario: Summary with promotion
- **GIVEN** services in the cart with an active promotion
- **WHEN** the user views the booking form
- **THEN** the UI SHALL display: subtotal, promotion discount line (e.g., "Buy 2 Get 1 Free: -€30"), and total

#### Scenario: Summary without promotion
- **GIVEN** services in the cart with no promotions
- **WHEN** the user views the booking form
- **THEN** the UI SHALL display the total amount (no discount line needed)

### Requirement: Quantity-Aware Availability Requests
The frontend SHALL send quantity information alongside service IDs when fetching availability, so the backend can compute correct total durations for time-slot selection.

#### Scenario: Fetching availability with quantities
- **WHEN** the user has Service A (qty=3, 30min each) and Service B (qty=1, 60min each) in the cart
- **THEN** the availability request SHALL include quantity data
- **AND** the backend SHALL compute `total_duration = 3×30 + 1×60 = 150` minutes
- **AND** only time slots with at least 150 minutes of free time SHALL be returned

#### Scenario: Fetching availability with quantity=1 (backward compatible)
- **WHEN** the frontend sends a request without quantity data
- **THEN** the backend SHALL default all quantities to 1 (existing behavior)