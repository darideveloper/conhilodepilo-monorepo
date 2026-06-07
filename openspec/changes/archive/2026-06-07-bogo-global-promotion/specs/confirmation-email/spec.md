## MODIFIED Requirements

### Requirement: Email contains service details and appointment info
The email SHALL include client name, service names with quantities, appointment date, start time, end time, and any special requests. Service names SHALL be rendered with quantity (e.g., "Eyebrow Threading ×3") and shown alongside their subtotal (unit price × quantity).

#### Scenario: All booking details rendered in email
- **WHEN** a confirmation email is sent
- **THEN** the email body contains: client name, list of services with quantities (e.g. "Eyebrow Threading ×3"), each service's subtotal, date in DD/MM/YYYY format, time range (HH:MM - HH:MM), and special requests text

#### Scenario: Plain-text fallback is included
- **WHEN** a confirmation email is sent
- **THEN** the email has both `text/plain` and `text/html` alternatives

## ADDED Requirements

### Requirement: Email shows pricing breakdown with discount
The email SHALL display a price summary section showing the original subtotal, any promotional discount, and the final total. When no discount applies, only the total is shown.

#### Scenario: Email shows price summary with discount
- **GIVEN** a booking was created with a promotional discount (e.g. Buy 2 Get 1 Free)
- **WHEN** the confirmation email is sent
- **THEN** the email SHALL display: Subtotal (sum of all line subtotals), Discount amount (e.g. "-€30.00"), and Total amount

#### Scenario: Email shows total only when no discount
- **GIVEN** a booking was created without any promotional discount
- **WHEN** the confirmation email is sent
- **THEN** the email SHALL display the total amount
- **AND** SHALL NOT show a discount line

### Requirement: Email fetches service data from through model
The confirmation email SHALL fetch service line items from `BookingServiceThrough` (via `booking.booking_services.all()`) instead of `booking.services.all()`, to access stored `quantity` and `unit_price` per service.

#### Scenario: Email renders quantity and unit price from through model
- **GIVEN** a booking with Service A × 3 at a stored unit_price of €30.00
- **WHEN** `send_confirmation_email()` is called
- **THEN** the service list SHALL include `quantity=3` and `unit_price=30.00` from the through model
- **AND** the subtotal SHALL be calculated as `3 × 30.00 = 90.00`
