## Context

Confirmation emails are built in `dashboard/utils/email.py::_build_base_context`, which is shared by `send_confirmation_email` and `send_gift_confirmation_emails`. It formats the appointment with:

```python
"date": booking.start_time.strftime("%d/%m/%Y"),
"start_time": booking.start_time.strftime("%H:%M"),
"end_time": booking.end_time.strftime("%H:%M") if booking.end_time else "",
```

`strftime` performs no timezone conversion. The project runs `USE_TZ=True` with `TIME_ZONE=Europe/Madrid`, so PostgreSQL stores the instant in UTC and a booking loaded from the database is UTC-aware. The bug surfaces on the pre-paid path: `StripeWebhookView` reloads the booking with `Booking.objects.get(...)` (`views.py:332`) and then sends the email, so the raw UTC value is printed (12:15 Madrid → 11:15). The direct post-paid path passes the in-memory object whose `tzinfo` is still `Europe/Madrid` from `timezone.make_aware`, which is why it looks correct today.

`utils/google_calendar.py` already calls `timezone.localtime(...)` before serializing, which is why the calendar event instant is correct. The email path is the only place that skipped the conversion.

## Goals / Non-Goals

**Goals:**
- Render `date`, `start_time`, and `end_time` in the company's local timezone for every client email.
- Fix both the DB-loaded (webhook) and in-memory paths with a single change.
- Add a regression test that exercises the DB-loaded path.

**Non-Goals:**
- Changing Google Calendar behavior (verified correct).
- Changing duration calculation (verified correct: `Σ duration_minutes × quantity`).
- Adding send retries/queues, changing the API response format, or redesigning the email template.
- Changing the per-service "Duración" column display.

## Decisions

**Decision: convert with `timezone.localtime()` inside `_build_base_context` before formatting.**
- Rationale: this is the single choke point feeding HTML and plain text for all variants, so one change fixes every path and both the in-memory and DB-loaded cases.
- Alternative considered: Django template filters (e.g. `{{ start_time|date:"H:i" }}`). Rejected — the plain-text body is built in Python, not the template, and template filters would leave it wrong.
- Alternative considered: localize a copy of the booking in each caller (`send_confirmation_email`, `send_gift_confirmation_emails`). Rejected — more call sites to keep in sync, and none of them fixes the shared context builder directly.

**Decision: derive the timezone from `settings.TIME_ZONE` via Django's `timezone.localtime()`.**
- `timezone.localtime()` uses the current active timezone, which defaults to `settings.TIME_ZONE`; no new setting is introduced. This matches the existing pattern in `utils/google_calendar.py`.

**Decision: guard `end_time` for `None` before converting.**
- Keep the existing conditional so bookings without an `end_time` still render an empty string.

## Risks / Trade-offs

- [A caller could later activate a different timezone via `timezone.activate()`] → Mitigation: if that ever happens, pass the zone explicitly: `timezone.localtime(booking.start_time, zoneinfo.ZoneInfo(settings.TIME_ZONE))`. No code activates another timezone today.
- [Existing broken emails are not retroactively fixed] → Mitigation: the fix applies to all future sends; affected bookings can be re-sent manually. There is no email queue/retry in the system, which is out of scope here.
- [Tests that send the in-memory object would pass before the fix] → Mitigation: the new regression test must reload the booking from the database before sending, matching the webhook path.

## Migration Plan

Code-only, backward compatible. Deploy the dashboard service; no database migration and no data backfill. Rollback is the previous deploy. Post-deploy verification: send or re-trigger one pre-paid booking and confirm the email shows local time.

## Open Questions

None blocking.
