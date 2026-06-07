# confirmation-email Specification

## Purpose
Defines the email notification system for booking confirmations. This delta adds dual-email support for gift bookings and modifies existing requirements to account for role-specific email dispatch.

## MODIFIED Requirements

### Requirement: Send branded HTML confirmation email upon booking confirmation
The system SHALL send branded HTML email(s) when a booking is confirmed (post-paid) or marked as paid (pre-paid). For gift bookings, two emails SHALL be sent: one to the buyer and one to the recipient. For non-gift bookings, one email SHALL be sent to the client.

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
- **AND** a failure for one email SHALL NOT prevent the other from being sent

### Requirement: Admin notification via BCC
The system SHALL BCC a copy of BOTH emails to all addresses in `settings.EMAILS_NOTIFICATIONS` whenever client emails are sent.

#### Scenario: Admin BCC on gift booking
- **WHEN** two emails are sent for a gift booking
- **THEN** both emails SHALL include BCC to `settings.EMAILS_NOTIFICATIONS`

## ADDED Requirements

### Requirement: Buyer email clearly identifies gift purchase
The buyer's confirmation email SHALL state that the booking was purchased as a gift and SHALL include the recipient's name.

#### Scenario: Buyer email shows gift context
- **WHEN** a buyer confirmation email is sent for a gift booking
- **THEN** the subject or body SHALL clearly indicate "Compraste un regalo para [recipient_name]"
- **AND** the email SHALL include the recipient's name and appointment details

### Requirement: Recipient email clearly identifies gift receipt
The recipient's notification email SHALL state that they received a gift and SHALL include the buyer's name.

#### Scenario: Recipient email shows gifter context
- **WHEN** a recipient notification email is sent for a gift booking
- **THEN** the subject or body SHALL clearly indicate "Has recibido un regalo de [buyer_name]"
- **AND** the email SHALL include the buyer's name and appointment details

### Requirement: Email content differs by role (buyer vs recipient)
The email template SHALL accept a `role` parameter (`"buyer"` or `"recipient"`) to render role-specific copy while sharing the same booking details (services, date, time, location).

#### Scenario: Buyer email includes purchase confirmation language
- **WHEN** rendering the buyer's email
- **THEN** the greeting SHALL address the buyer
- **AND** the body SHALL confirm the gift purchase
- **AND** the WhatsApp CTA SHALL be for the buyer's needs

#### Scenario: Recipient email includes gift surprise language
- **WHEN** rendering the recipient's email
- **THEN** the greeting SHALL address the recipient
- **AND** the body SHALL announce the gift
- **AND** the WhatsApp CTA SHALL offer rescheduling assistance
