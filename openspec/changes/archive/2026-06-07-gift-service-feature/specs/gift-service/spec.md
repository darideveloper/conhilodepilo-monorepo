# gift-service Specification

## Purpose
Defines the gift service feature allowing buyers to book services for other recipients, with proper data tracking and dual-email notification.

## ADDED Requirements

### Requirement: Gift toggle in booking form
The booking form (step 3) MUST present a checkbox labeled "¿Es un servicio de regalo?" before the privacy policy acceptance. When checked, two additional fields SHALL appear: recipient name and recipient email.

#### Scenario: Gift checkbox renders by default unchecked
- **WHEN** the booking form step 3 loads
- **THEN** the gift checkbox MUST be visible and unchecked
- **AND** the recipient name and email fields MUST NOT be visible

#### Scenario: Checking gift toggle reveals recipient fields
- **WHEN** the user checks the "¿Es un servicio de regalo?" checkbox
- **THEN** recipient name and recipient email input fields SHALL animate into view below the checkbox

#### Scenario: Unchecking gift toggle hides recipient fields
- **WHEN** the user unchecks the gift checkbox
- **THEN** the recipient name and email fields SHALL be hidden
- **AND** any entered values SHALL be cleared

### Requirement: Recipient fields required when gift enabled
When the gift checkbox is checked, the recipient name and email fields MUST be required for form submission.

#### Scenario: Submit blocked without recipient data
- **WHEN** the gift checkbox is checked
- **AND** the user attempts to submit with empty recipient name or email
- **THEN** the form SHALL display validation errors
- **AND** submission SHALL be prevented

### Requirement: Client name maps to final service recipient
The `client_name` and `client_email` on the Booking model SHALL always represent the person who will actually receive the service. When the booking is not a gift, they equal the buyer's name and email. When it is a gift, they equal the gift recipient's name and email.

#### Scenario: Non-gift booking maps buyer as client
- **WHEN** a booking is created with `is_gift=false`
- **THEN** `client_name` SHALL equal `buyer_name`
- **AND** `client_email` SHALL equal `buyer_email`

#### Scenario: Gift booking maps recipient as client
- **WHEN** a booking is created with `is_gift=true`
- **THEN** `client_name` SHALL equal `recipient_name`
- **AND** `client_email` SHALL equal `recipient_email`

### Requirement: Dual-email notification for gift bookings
When a gift booking is confirmed (post-paid) or paid (pre-paid), the system SHALL send two separate emails: one to the buyer confirming the purchase, and one to the recipient notifying them of the gift.

#### Scenario: Buyer receives confirmation email on gift booking
- **WHEN** a gift booking is confirmed or paid
- **THEN** an email SHALL be sent to `booking.buyer_email`
- **AND** the email SHALL clearly state the buyer purchased a gift for the recipient
- **AND** the email SHALL include the recipient's name and the appointment details

#### Scenario: Recipient receives gift notification email
- **WHEN** a gift booking is confirmed or paid
- **THEN** an email SHALL be sent to `booking.client_email` (the recipient)
- **AND** the email SHALL clearly state the recipient received a gift from the buyer
- **AND** the email SHALL include the buyer's name and the appointment details

#### Scenario: Non-gift booking sends single email
- **WHEN** a non-gift booking is confirmed or paid
- **THEN** exactly one email SHALL be sent to `booking.client_email`
- **AND** the email SHALL NOT mention any gift-related information

### Requirement: Dashboard displays gift badge and buyer info
The admin booking list SHALL display a visual badge indicating gift bookings and SHALL show both buyer and recipient information clearly in the detail view.

#### Scenario: Gift badge in booking list
- **WHEN** a booking with `is_gift=true` is displayed in the admin list
- **THEN** it SHALL show a visible "🎁 Regalo" badge or indicator

#### Scenario: Buyer and recipient shown in detail
- **WHEN** viewing a gift booking in the admin detail
- **THEN** both `buyer_name`/`buyer_email` and `recipient_name`/`recipient_email` SHALL be displayed
- **AND** the field SHALL be labeled clearly to distinguish roles
