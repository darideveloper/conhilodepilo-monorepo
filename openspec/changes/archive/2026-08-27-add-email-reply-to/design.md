## Context

The dashboard sends booking confirmation and gift emails through the SMTP account `no-reply@conhilodepilo.com` (see `onboard-conhilodepilo-email`). All send paths funnel through the single helper `_send_email` in `dashboard/utils/email.py`, which builds an `EmailMultiAlternatives` with `from_email=settings.EMAIL_FROM` and no `Reply-To` header. `no-reply@` has no alias/forward to `info@`, so client replies are silently lost. Email config is env-first (`EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAILS_NOTIFICATIONS` in `settings.py`).

## Goals / Non-Goals

**Goals:**
- Client replies to any booking email land in a monitored inbox (`info@conhilodepilo.com`).
- Reply-To applied to all client-facing email types (confirmation, gift recipient, gift buyer) in one place.

**Non-Goals:**
- Forwarding/bounce handling at the Stalwart server level (aliases, Sieve rules) — the `no-reply@` account stays unmonitored and isolated.
- Changing the sender (`from`) address; sending continues from `no-reply@`.

## Decisions

1. **`Reply-To` header set in `_send_email` (the shared helper).** All three send paths (`send_confirmation_email`, gift recipient, gift buyer) route through it, so one change covers every email. *Alternative considered:* per-call `reply_to` arguments — unnecessary duplication since the address is identical for all client emails.
2. **Configurable `EMAIL_REPLY_TO` env var, default `info@conhilodepilo.com`.** Matches the project's env-first convention and lets the operator override without a deploy. *Alternative considered:* hardcoding the address in `email.py` — couples code to a domain and can't be overridden.
3. **No Stalwart change.** A server-side forward on `no-reply@` would also catch bounces, test emails, and auto-responders, polluting `info@`; the header approach is standard and keeps the no-reply account purpose-built.

## Risks / Trade-offs

- [**Reply-To ignored by some clients/auto-responders**] → Accepted; every mainstream mail client honors `Reply-To`. Server-side forward can be added later if needed.
- [**Custom `EMAIL_REPLY_TO` left unset → default could be wrong for another deployment**] → Default matches the live company inbox; example env files document the variable.

## Migration Plan

1. Add `EMAIL_REPLY_TO` to `settings.py` (env-first, default `info@conhilodepilo.com`).
2. Add `reply_to` to `_send_email`'s `EmailMultiAlternatives`.
3. Document `EMAIL_REPLY_TO` in the example env files (generic placeholder).
4. Add tests asserting the header on all three email types and the custom-address override.
5. Deploy = normal dashboard release; no data migration, no env change required (default already correct).

**Rollback:** remove the `reply_to` kwarg / setting; no persistent state involved.

## Open Questions

- None.