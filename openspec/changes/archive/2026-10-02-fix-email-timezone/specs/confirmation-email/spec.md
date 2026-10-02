## ADDED Requirements

### Requirement: Appointment times rendered in company local timezone
Client confirmation emails SHALL render the appointment date, start time, and end time converted to the company's configured local timezone (`settings.TIME_ZONE`, e.g. `Europe/Madrid`), not the raw UTC value stored in the database. This SHALL apply to the HTML and plain-text bodies and to all email variants (regular booking, gift buyer, gift recipient), including bookings loaded from the database (for example after a Stripe webhook transitions a booking to `PAID`).

#### Scenario: DB-loaded booking renders local start time
- **GIVEN** a booking stored with `start_time` at `11:15 UTC` and `settings.TIME_ZONE` set to `Europe/Madrid`
- **WHEN** a confirmation email is sent
- **THEN** the email SHALL show `12:15` as the start time
- **AND** SHALL NOT show `11:15`

#### Scenario: Local end time and duration preserved
- **GIVEN** a booking stored with `start_time` at `11:15 UTC` and `end_time` at `15:15 UTC` and `settings.TIME_ZONE` set to `Europe/Madrid`
- **WHEN** a confirmation email is sent
- **THEN** the email SHALL show the range `12:15 - 16:15`
- **AND** the rendered duration SHALL remain 4 hours

#### Scenario: Local date rendered across midnight
- **GIVEN** a booking stored with `start_time` at `23:30 UTC` on 31 October and `settings.TIME_ZONE` set to `Europe/Madrid`
- **WHEN** a confirmation email is sent
- **THEN** the email SHALL show the date `01/11` (1 November) and the start time `00:30`

#### Scenario: All email variants use local time
- **GIVEN** a gift booking stored at `11:15 UTC` and `settings.TIME_ZONE` set to `Europe/Madrid`
- **WHEN** the buyer and gift recipient emails are sent
- **THEN** both emails SHALL show `12:15` as the start time
