## Why

The logo inside the email templates needs to be removed to simplify the email layout and keep the email headers clean, while keeping the company name title centered.

## What Changes

- Remove the logo image rendering from the booking confirmation email template ([booking_confirmation.html](file:///develop/monorepos/conhilorepilo/dashboard/project/templates/email/booking_confirmation.html)).
- Ensure the company title remains centered in the email header.
- Remove the logo URL builder helper `_build_logo_url` and its context key `logo_url` from the email utilities ([email.py](file:///develop/monorepos/conhilorepilo/dashboard/utils/email.py)).
- Clean up tests verifying the logo URL building in [tests_email.py](file:///develop/monorepos/conhilorepilo/dashboard/booking/tests_email.py).

## Capabilities

### New Capabilities

*(None)*

### Modified Capabilities

- `confirmation-email`: The requirement to display the company logo in the email header and build an absolute logo URL is removed.

## Impact

- Email Templates: [booking_confirmation.html](file:///develop/monorepos/conhilorepilo/dashboard/project/templates/email/booking_confirmation.html)
- Django Backend Utils: [email.py](file:///develop/monorepos/conhilorepilo/dashboard/utils/email.py)
- Django Backend Tests: [tests_email.py](file:///develop/monorepos/conhilorepilo/dashboard/booking/tests_email.py)
