# confirmation-email Specification

## Purpose
TBD - created by archiving change bogo-global-promotion. Update Purpose after archive.
## Requirements
### Requirement: Send branded HTML confirmation email upon booking confirmation
The system SHALL send branded HTML email(s) when a booking is confirmed (post-paid) or marked as paid (pre-paid). For gift bookings, two emails SHALL be sent: one to the buyer and one to the recipient. For non-gift bookings, one email SHALL be sent to the client. The email SHALL use the SMTP configuration from environment variables and branding from CompanyProfile.

#### Scenario: Single email sent on non-gift booking
- **WHEN** a non-gift booking is created with `status=CONFIRMED` in `CreateBookingView`
- **THEN** the system sends exactly one HTML email to `booking.client_email`

#### Scenario: Two emails sent on gift booking creation
- **WHEN** a gift booking is created with `status=CONFIRMED` in `CreateBookingView`
- **THEN** the system sends one HTML email to `booking.buyer_email` (buyer confirmation)
- **AND** one HTML email to `booking.client_email` (recipient notification)

#### Scenario: Two emails sent on gift payment completion
- **WHEN** the Stripe webhook transitions a gift booking from `PENDING` to `PAID`
- **THEN** the system sends one HTML email to `booking.buyer_email`
- **AND** one HTML email to `booking.client_email`

#### Scenario: Email failure does not block booking flow
- **WHEN** the SMTP server is unreachable during email sending
- **THEN** the booking is still confirmed and the response is returned normally
- **AND** the error is logged

### Requirement: Admin notification via BCC
The system SHALL BCC a copy of BOTH emails to all addresses in `settings.EMAILS_NOTIFICATIONS` whenever client emails are sent.

#### Scenario: Admin BCC on gift booking
- **WHEN** two emails are sent for a gift booking
- **THEN** both emails SHALL include BCC to `settings.EMAILS_NOTIFICATIONS`

### Requirement: Buyer email clearly identifies gift purchase
The buyer's confirmation email SHALL state that the booking was purchased as a gift and SHALL include the recipient's name.

#### Scenario: Buyer email shows gift context
- **WHEN** a buyer confirmation email is sent for a gift booking
- **THEN** the subject or body SHALL clearly indicate "Has regalado una cita a [recipient_name]"
- **AND** the email SHALL include the recipient's name and appointment details

### Requirement: Recipient email clearly identifies gift receipt
The recipient's notification email SHALL state that they received a gift and SHALL include the buyer's name.

#### Scenario: Recipient email shows gifter context
- **WHEN** a recipient notification email is sent for a gift booking
- **THEN** the subject or body SHALL clearly indicate "Has recibido un regalo de [buyer_name]"
- **AND** the email SHALL include the buyer's name and appointment details

### Requirement: Email content and pricing differs by role (buyer vs recipient)
The email template SHALL accept a `role` parameter (`"buyer"` or `"recipient"`) to render role-specific copy. Buyer and regular booking emails SHALL include full service details with subtotals and a pricing summary. Gift recipient emails SHALL show services without prices and SHALL NOT include any pricing summary.

#### Scenario: Buyer email includes purchase confirmation language
- **WHEN** rendering the buyer's email
- **THEN** the greeting SHALL address the buyer
- **AND** the body SHALL confirm the gift purchase
- **AND** the WhatsApp CTA SHALL be for the buyer's needs
- **AND** the email SHALL include full pricing breakdown

#### Scenario: Recipient email includes gift surprise language
- **WHEN** rendering the recipient's email
- **THEN** the greeting SHALL address the recipient
- **AND** the body SHALL announce the gift
- **AND** the WhatsApp CTA SHALL offer rescheduling assistance
- **AND** the email SHALL NOT display any pricing information

### Requirement: Email contains service details and appointment info
The email SHALL include client name, service names with quantities, appointment date, start time, end time, and any special requests. Service names SHALL be rendered with quantity (e.g., "Eyebrow Threading ×3"). For buyer and regular booking emails, services SHALL be shown alongside their subtotal (unit price × quantity). For gift recipient emails, services SHALL be shown without subtotals.

#### Scenario: All booking details rendered in buyer and regular email
- **WHEN** a confirmation email is sent to a buyer or regular client
- **THEN** the email body contains: client name, list of services with quantities (e.g. "Eyebrow Threading ×3"), each service's subtotal, date in DD/MM/YYYY format, time range (HH:MM - HH:MM), and special requests text

#### Scenario: Services shown without prices in gift recipient email
- **WHEN** a recipient notification email is sent for a gift booking
- **THEN** the email body contains: client name, list of services with quantities (e.g. "Eyebrow Threading ×3"), appointment date, time range, and special requests text
- **AND** SHALL NOT include per-service subtotals

#### Scenario: Plain-text fallback is included
- **WHEN** a confirmation email is sent
- **THEN** the email has both `text/plain` and `text/html` alternatives

### Requirement: WhatsApp contact link in email footer
The email SHALL include a WhatsApp link as a call-to-action in the footer with the text "¿Necesitas ayuda o quieres reagendar? Da click aquí". The link SHALL be built from `CompanyProfile.contact_phone`.

#### Scenario: WhatsApp link rendered from CompanyProfile phone
- **WHEN** `CompanyProfile.contact_phone` is set to a valid number
- **THEN** the email footer contains `https://wa.me/<digits>` with the digits extracted from `contact_phone`

#### Scenario: WhatsApp link omitted when no phone configured
- **WHEN** `CompanyProfile.contact_phone` is `None` or empty
- **THEN** the WhatsApp section is omitted from the email

### Requirement: Email uses company branding from CompanyProfile
The email SHALL use the company name, brand color, and social media URLs from `CompanyProfile`. The company logo SHALL NOT be displayed in the email template.

#### Scenario: Company name appears in email header
- **WHEN** a confirmation email is sent
- **THEN** the email header displays the company name from `CompanyProfile`
- **AND** the company logo is not included or rendered

#### Scenario: Social links rendered in email footer
- **WHEN** a confirmation email is sent
- **THEN** the email footer contains links to Instagram, TikTok, and Facebook from `CompanyProfile`

### Requirement: Email shows pricing breakdown with discount
The email SHALL display a price summary section showing the original subtotal, any promotional discount, and the final total. When no discount applies, only the total is shown. This pricing summary SHALL be hidden in gift recipient emails.

#### Scenario: Email shows price summary with discount
- **GIVEN** a booking was created with a promotional discount (e.g. Buy 2 Get 1 Free)
- **WHEN** the confirmation email is sent to a buyer or regular client
- **THEN** the email SHALL display: Subtotal (sum of all line subtotals), Discount amount (e.g. "-€30.00"), and Total amount

#### Scenario: Email shows total only when no discount
- **GIVEN** a booking was created without any promotional discount
- **WHEN** the confirmation email is sent to a buyer or regular client
- **THEN** the email SHALL display the total amount
- **AND** SHALL NOT show a discount line

#### Scenario: Pricing hidden in gift recipient email
- **GIVEN** a gift booking with any pricing
- **WHEN** the recipient notification email is sent
- **THEN** the email SHALL NOT display any pricing information (no Subtotal column, no per-service subtotals, no discount, no total)

### Requirement: Email fetches service data from through model
The confirmation email SHALL fetch service line items from `BookingServiceThrough` (via `booking.booking_services.all()`) instead of `booking.services.all()`, to access stored `quantity` and `unit_price` per service.

#### Scenario: Email renders quantity and unit price from through model
- **GIVEN** a booking with Service A × 3 at a stored unit_price of €30.00
- **WHEN** `send_confirmation_email()` is called
- **THEN** the service list SHALL include `quantity=3` and `unit_price=30.00` from the through model
- **AND** the subtotal SHALL be calculated as `3 × 30.00 = 90.00`

