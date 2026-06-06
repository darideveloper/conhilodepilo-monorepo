## 1. Email Service Module

- [x] 1.1 Create `dashboard/utils/email.py` with `send_confirmation_email(booking)` function
- [x] 1.2 Add `_clean_phone()` helper to strip non-digits for WhatsApp URL
- [x] 1.3 Add `_build_whatsapp_url()` helper that reads `CompanyProfile.contact_phone`
- [x] 1.4 Handle `CompanyProfile.get_solo()` lookup for branding context (logo, brand_color, name, phone, social URLs)
- [x] 1.5 Read `settings.EMAILS_NOTIFICATIONS` and add admin emails as BCC on the outgoing email
- [x] 1.6 Wrap email sending in try/except with logging, never raise to caller

## 2. Email HTML Template

- [x] 2.1 Create `dashboard/project/templates/email/booking_confirmation.html` with inline styles
- [x] 2.2 Build email header with company logo and brand color
- [x] 2.3 Build email body with client greeting and service list
- [x] 2.4 Build appointment details section (date, time range)
- [x] 2.5 Build WhatsApp footer CTA: "¿Necesitas ayuda o quieres reagendar? Da click aquí" linking to `https://wa.me/<digits>`
- [x] 2.6 Build footer with social links (Instagram, TikTok, Facebook) and company info
- [x] 2.7 Attach HTML alternative to `EmailMultiAlternatives` with plain-text fallback

## 3. Wire Email into Booking Flows

- [x] 3.1 Import and call `send_confirmation_email(booking)` in `CreateBookingView.post()` after booking is created with `status=CONFIRMED`
- [x] 3.2 Import and call `send_confirmation_email(booking)` in `StripeWebhookView.post()` after booking transitions to `PAID`
- [x] 3.3 Ensure email call is wrapped in `transaction.on_commit()` (matching the Google Calendar sync pattern) so it only fires after DB commit

## 4. Image URL Handling

- [x] 4.1 Resolve absolute logo URL using `settings.HOST` env var for email context (no request object available at send time)
- [x] 4.2 Add fallback: skip logo in template if URL cannot be resolved

## 5. Testing

- [x] 5.1 Write unit tests for `send_confirmation_email()` in `dashboard/booking/tests_email.py`
- [x] 5.2 Test that email is called when booking created as CONFIRMED
- [x] 5.3 Test that email is called when Stripe webhook transitions booking to PAID
- [x] 5.4 Test that email failure does not raise exception in views
- [x] 5.5 Test that WhatsApp URL is correctly formatted from `CompanyProfile.contact_phone`
