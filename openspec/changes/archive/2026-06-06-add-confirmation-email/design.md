## Context

The dashboard already has SMTP env vars configured, a `Booking.client_email` field, and a `CompanyProfile` singleton with `contact_phone`, `logo`, `brand_color`, and social URLs. It also has a `TestEmailView` endpoint for validating SMTP credentials.

There are two booking confirmation flows:
1. **Post-paid:** `CreateBookingView` creates the booking with `status=CONFIRMED` directly
2. **Pre-paid (Stripe):** `StripeWebhookView` transitions `PENDING → PAID`

Neither flow sends any notification to the client. A `TestEmailView` exists for SMTP debugging but is not wired into business logic.

## Goals / Non-Goals

**Goals:**
- Send a branded HTML confirmation email to the client upon booking confirmation (post-paid) or payment completion (pre-paid)
- Include service names, date, time, social links, and a WhatsApp contact link in the email
- Source branding (logo, colors) and WhatsApp number from `CompanyProfile` singleton
- BCC a copy of the confirmation email to admin emails configured in `settings.EMAILS_NOTIFICATIONS`
- Follow the existing explicit-call pattern rather than adding new signals
- Write auto-generated plain-text fallback alongside HTML

**Non-Goals:**
- Cancellation or rescheduling emails (future)
- Email queue, retry, or delivery tracking
- Unsubscribe mechanism
- Multi-language email support (Spanish only)

## Decisions

**1. Explicit calls in views over signals.**
The Google Calendar sync uses signals because it fires from multiple status transitions (CONFIRMED, PAID, CANCELLED). The email only fires from two specific, well-known points. Calling `send_confirmation_email(booking)` directly in `CreateBookingView` and `StripeWebhookView` is simpler to trace, test, and debug.

**2. Single HTML template with inline styles.**
Email client CSS support is fragmented. Using inline styles guarantees consistent rendering across Gmail, Outlook, and mobile clients. The template is a single `booking_confirmation.html` file under `project/templates/email/`.

**3. WhatsApp URL from `CompanyProfile.contact_phone`.**
The landing page already uses this pattern: strip non-digits, build `https://wa.me/<digits>`. The email module reuses the same logic rather than adding a dedicated `whatsapp_number` field.

**4. `EmailMultiAlternatives` for HTML + plain-text fallback.**
Django's `EmailMultiAlternatives` allows attaching an HTML alternative while auto-generating a plain-text version. Better deliverability than `send_mail` alone.

**5. BCC admin emails on the same message, not a separate send.**
The `EMAILS_NOTIFICATIONS` env var holds comma-separated admin emails. Adding them as BCC on the client confirmation email is simpler than sending two separate messages — the admin gets the same branded HTML with full booking details. No separate template or send logic needed.

**6. Wrap send in try/except, log failure, don't block the response.**
Email sending is a side-effect that should never break the booking flow. If SMTP is down, the booking is still confirmed; the error is logged (or silently swallowed in the views). The `TestEmailView` remains the tool for debugging SMTP issues.

## Risks / Trade-offs

- **SMTP downtime → email not sent, silently ignored.** → Log errors via Django's `logger`; admin can resend via TestEmailView or manually.
- **Template rendering error at send time.** → The `render_to_string` call is inside the try/except; booking confirmation is never blocked by email failure.
- **Phone number missing or unformatted in CompanyProfile.** → `_clean_phone` handles None/empty; WhatsApp link just won't render if no number configured.
- **Images (logo) require absolute URLs in email.** → Use `settings.HOST` to build an absolute URL from `CompanyProfile.logo`. If `HOST` contains "localhost" (local dev), the logo is skipped to avoid broken images. In production with a public `HOST`, the logo renders correctly. The header still shows the company name with brand color as fallback.
