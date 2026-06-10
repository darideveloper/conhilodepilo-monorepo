## ADDED Requirements

*None*

## MODIFIED Requirements

### Requirement: Email shows pricing breakdown with discount

**Updated text:** The email SHALL display a price summary section showing the original subtotal, any promotional discount, and the final total. When no discount applies, only the total is shown. This pricing summary SHALL be hidden in gift recipient emails (email_role="recipient"), while remaining visible in buyer and regular booking emails.

#### Scenario: Email shows price summary with discount
- **GIVEN** a booking was created with a promotional discount (e.g. Buy 2 Get 1 Free)
- **WHEN** the confirmation email is sent to a buyer or regular client
- **THEN** the email SHALL display: Subtotal (sum of all line subtotals), Discount amount (e.g. "-€30.00"), and Total amount

#### Scenario: Pricing hidden in gift recipient email
- **GIVEN** a gift booking with a promotional discount
- **WHEN** the recipient notification email is sent
- **THEN** the email SHALL NOT display any pricing information (no Subtotal column, no per-service subtotals, no discount, no total)

### Requirement: Email contains service details and appointment info

**Updated text:** The email SHALL include client name, service names with quantities, appointment date, start time, end time, and any special requests. Service names SHALL be rendered with quantity (e.g., "Eyebrow Threading ×3"). For buyer and regular booking emails, services SHALL be shown alongside their subtotal (unit price × quantity). For gift recipient emails, services SHALL be shown without subtotals (only name, quantity, and duration).

#### Scenario: All booking details rendered in buyer and regular email
- **WHEN** a confirmation email is sent to a buyer or regular client
- **THEN** the email body contains: client name, list of services with quantities (e.g. "Eyebrow Threading ×3"), each service's subtotal, date in DD/MM/YYYY format, time range (HH:MM - HH:MM), and special requests text

#### Scenario: Services shown without prices in gift recipient email
- **WHEN** a recipient notification email is sent for a gift booking
- **THEN** the email body contains: client name, list of services with quantities (e.g. "Eyebrow Threading ×3"), appointment date, time range, and special requests text
- **AND** SHALL NOT include per-service subtotals or any pricing summary

## REMOVED Requirements

*None*
