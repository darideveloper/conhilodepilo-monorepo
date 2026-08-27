## ADDED Requirements

### Requirement: Booking emails include Reply-To header
Client-facing booking emails (confirmation, gift recipient, gift buyer) SHALL include a `Reply-To` header so replies to the `no-reply@` sender address reach a monitored mailbox instead of sitting in the unmonitored `no-reply@` inbox. The Reply-To address SHALL be configurable via the `EMAIL_REPLY_TO` setting, which SHALL default to `info@conhilodepilo.com`.

#### Scenario: Confirmation email carries Reply-To header
- **WHEN** a non-gift booking confirmation email is sent to the client
- **THEN** the email SHALL include `Reply-To` set to the `EMAIL_REPLY_TO` address (default `info@conhilodepilo.com`)

#### Scenario: Gift recipient email carries Reply-To header
- **WHEN** a gift recipient notification email is sent
- **THEN** the email SHALL include `Reply-To` set to the `EMAIL_REPLY_TO` address

#### Scenario: Gift buyer email carries Reply-To header
- **WHEN** a gift buyer confirmation email is sent
- **THEN** the email SHALL include `Reply-To` set to the `EMAIL_REPLY_TO` address

#### Scenario: Custom Reply-To address is honored
- **GIVEN** `EMAIL_REPLY_TO` is set to a custom address (e.g. `custom@example.com`)
- **WHEN** any booking email is sent
- **THEN** the email SHALL include `Reply-To` set to that custom address