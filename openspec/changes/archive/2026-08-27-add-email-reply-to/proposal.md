## Why

Booking confirmation and gift emails are sent from `no-reply@conhilodepilo.com` (the dashboard's SMTP account). When a client replies to these emails, the reply lands in the `no-reply@` mailbox and is never seen by the team — `no-reply@` has no alias to `info@conhilodepilo.com`. Replies should be directed to the company's inbox.

## What Changes

- All booking confirmation and gift emails sent from the dashboard will carry a `Reply-To: info@conhilodepilo.com` header, so client replies reach the company inbox instead of the unmonitored `no-reply@` account.
- The Reply-To address becomes configurable via a new `EMAIL_REPLY_TO` environment variable (default `info@conhilodepilo.com`).
- Example env files document the new variable with a generic placeholder.
- Tests verify the header on regular and gift (recipient + buyer) emails.

## Capabilities

### New Capabilities

None — this is a requirement added to the existing confirmation email behavior.

### Modified Capabilities

- `confirmation-email`: add a requirement that every client-facing booking email SHALL include a `Reply-To` header pointing to the company inbox (default `info@conhilodepilo.com`).

## Impact

- `dashboard/project/settings.py` — add `EMAIL_REPLY_TO` setting (env-first, with default).
- `dashboard/utils/email.py` — set `reply_to` on the `EmailMultiAlternatives` used by all send functions (`_send_email`).
- `dashboard/.env.dev.example` / `dashboard/.env.prod.example` — document `EMAIL_REPLY_TO`.
- `dashboard/booking/tests_email.py` — assert `Reply-To` on confirmation and gift emails.