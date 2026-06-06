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
The email SHALL include client name, service names, appointment date, start time, end time, and any special requests.

#### Scenario: All booking details rendered in email
- **WHEN** a confirmation email is sent
- **THEN** the email body contains: client name, list of service names, date in DD/MM/YYYY format, time range (HH:MM - HH:MM), and special requests text

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
