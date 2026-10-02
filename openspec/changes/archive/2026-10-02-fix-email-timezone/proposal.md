## Why

Client confirmation emails render the appointment date and time in UTC (the raw stored value), so recipients see times shifted from the company's local timezone. A booking made for 12:15 in Madrid (`Europe/Madrid`, UTC+1) arrived in the email as `11:15`, and would be off by 2 hours in summer. The bug is confirmed for pre-paid bookings because the Stripe webhook reloads the booking from the database (UTC-aware) before sending; post-paid bookings only appear correct because they reuse the in-memory, timezone-aware object.

Note: the 4-hour duration and the Google Calendar event were investigated and are **correct** (the service is 60 min × quantity 4; the calendar instant is right, it was only displayed in a Mexico viewer timezone). This change is scoped to the email time rendering only.

## What Changes

- Render the appointment `date`, `start_time`, and `end_time` in the confirmation email in the company's configured local timezone (`settings.TIME_ZONE`) instead of raw UTC.
- Cover every email variant (regular, gift buyer, gift recipient) and both the HTML and plain-text bodies, since they all read the same context.
- Add regression tests that send an email for a booking reloaded from the database and assert the local wall-clock time.

No template, API, or data-model changes.

## Capabilities

### New Capabilities
<!-- None -->

### Modified Capabilities
- `confirmation-email`: appointment date and time must be rendered in the company's local timezone, including for bookings loaded from the database.

## Impact

- `dashboard/utils/email.py` — `_build_base_context` (single choke point shared by all email variants).
- `dashboard/booking/tests_email.py` — regression tests for local-time rendering.
- No changes to `dashboard/project/templates/email/booking_confirmation.html`, the booking API, or the database.
