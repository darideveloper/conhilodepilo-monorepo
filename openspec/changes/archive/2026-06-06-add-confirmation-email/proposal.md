## Why

Clients who book services receive no confirmation email after payment or booking confirmation. The success page falsely claims "we sent the details to your email." This leaves clients without a record of their appointment, creates confusion, and undermines trust.

## What Changes

- Add an email service module (`dashboard/utils/email.py`) to send branded HTML confirmation emails
- Create an HTML email template with company branding, service details, date/time, social links, and a WhatsApp contact link
- Wire email sending into the two booking confirmation flows: `CreateBookingView` (post-paid → CONFIRMED) and `StripeWebhookView` (pre-paid → PAID)
- Add a utility function to format `contact_phone` into a WhatsApp URL (`https://wa.me/<digits>`)
- Send a BCC copy of the confirmation email to admin emails configured in `EMAILS_NOTIFICATIONS` env var
- Add unit tests for the email module

## Capabilities

### New Capabilities
- `confirmation-email`: Sends branded HTML confirmation emails to clients upon booking confirmation or payment completion. Includes service details, appointment date/time, social links, and WhatsApp contact link sourced from CompanyProfile. BCC-copies admin emails from `EMAILS_NOTIFICATIONS` env var.

### Modified Capabilities
*(None — this is a net-new capability)*

## Impact

- **New file:** `dashboard/utils/email.py` — email service module
- **New file:** `dashboard/project/templates/email/booking_confirmation.html` — email template
- **Modified:** `dashboard/booking/views.py` — add email call in `CreateBookingView` and `StripeWebhookView`
- **No new dependencies** — uses Django stdlib `django.core.mail.EmailMultiAlternatives`
- **No env changes needed** — SMTP vars already configured
