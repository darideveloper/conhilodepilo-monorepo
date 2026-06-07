# confirmation-email Specification

## Purpose
TBD - created by archiving change bogo-global-promotion. Update Purpose after archive.
## Requirements
### Requirement: Send branded HTML confirmation email upon booking confirmation
The system SHALL send a branded HTML email to the client when a booking is confirmed (post-paid) or marked as paid (pre-paid). The email SHALL use the SMTP configuration from environment variables and branding from CompanyProfile.

#### Scenario: Email sent on post-paid booking creation
- **WHEN** a booking is created with `status=CONFIRMED` in `CreateBookingView`
- **THEN** the system sends an HTML email to `booking.client_email`

#### Scenario: Email sent on pre-paid payment completion
- **WHEN** the Stripe webhook transitions a booking from `PENDING` to `PAID`
- **THEN** the system sends an HTML email to `booking.client_email`

#### Scenario: Email failure does not block booking flow
- **WHEN** the SMTP server is unreachable during email sending
- **THEN** the booking is still confirmed and the response is returned normally
- **AND** the error is logged

### Requirement: Email contains service details and appointment info
The email SHALL include client name, service names with quantities, appointment date, start time, end time, and any special requests. Service names SHALL be rendered with quantity (e.g., "Eyebrow Threading ×3") and shown alongside their subtotal (unit price × quantity).

#### Scenario: All booking details rendered in email
- **WHEN** a confirmation email is sent
- **THEN** the email body contains: client name, list of services with quantities (e.g. "Eyebrow Threading ×3"), each service's subtotal, date in DD/MM/YYYY format, time range (HH:MM - HH:MM), and special requests text

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
The email SHALL use the company name, logo, brand color, and social media URLs from `CompanyProfile`.

#### Scenario: Company name and logo appear in email header
- **WHEN** a confirmation email is sent
- **THEN** the email header displays the company name and logo from `CompanyProfile`

#### Scenario: Logo URL is absolute
- **WHEN** the email template renders the logo image
- **THEN** the `src` attribute is an absolute URL (not a relative path)

#### Scenario: Social links rendered in email footer
- **WHEN** a confirmation email is sent
- **THEN** the email footer contains links to Instagram, TikTok, and Facebook from `CompanyProfile`

### Requirement: Admin notification via BCC
The system SHALL BCC a copy of the confirmation email to all emails in `settings.EMAILS_NOTIFICATIONS` whenever a client confirmation email is sent.

#### Scenario: Admin BCC sent alongside client email
- **WHEN** a confirmation email is sent to `booking.client_email`
- **THEN** the same email SHALL also be BCC'd to every address in `settings.EMAILS_NOTIFICATIONS`

#### Scenario: No admin BCC when EMAILS_NOTIFICATIONS is empty
- **WHEN** `settings.EMAILS_NOTIFICATIONS` is empty or contains only empty strings
- **THEN** no BCC SHALL be added to the email

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

