## 1. Fix email time rendering

- [x] 1.1 In `dashboard/utils/email.py`, import `django.utils.timezone` alongside the existing imports.
- [x] 1.2 In `_build_base_context`, convert `booking.start_time` and `booking.end_time` with `timezone.localtime(...)` before formatting, and use the converted values for `date`, `start_time`, and `end_time`.
- [x] 1.3 Keep the existing `None` guard for `end_time` so bookings without an end time still render an empty string.

## 2. Regression tests

All new tests SHALL set `@override_settings(TIME_ZONE="Europe/Madrid")` explicitly so they are deterministic regardless of the ambient environment, and SHALL force the DB-loaded path with `booking.refresh_from_db()`.

- [x] 2.1 In `dashboard/booking/tests_email.py`, add a test that creates a booking at `11:15 UTC`, calls `refresh_from_db()`, sends the email, and asserts `12:15` (not `11:15`) in both the HTML and plain-text bodies.
- [x] 2.2 Add a test asserting the local end time (`12:15 - 16:15` for `11:15 UTC - 15:15 UTC`) is rendered and the implied duration remains 4 hours.
- [x] 2.3 Add a test for date rollover: a booking at `23:30 UTC` on 31 October renders date `01/11` and start time `00:30`.
- [x] 2.4 Add a test confirming both gift buyer and gift recipient emails render `12:15` for a DB-loaded booking.

## 3. Verify

- [x] 3.1 Run the email test module from the `dashboard/` directory: `venv/bin/python manage.py test booking.tests_email`, and confirm all tests pass (including the pre-existing `test_plain_text_body_contains_booking_details`, which must still see `10:00` for the in-memory booking).
- [x] 3.2 Confirm no changes are needed to `booking_confirmation.html`, the booking API, or the database.
