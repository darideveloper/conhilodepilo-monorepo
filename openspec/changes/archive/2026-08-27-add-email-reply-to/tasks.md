## 1. Settings & Configuration

- [x] 1.1 Add `EMAIL_REPLY_TO` setting to `dashboard/project/settings.py` (env-first, default `info@conhilodepilo.com`)
- [x] 1.2 Add `EMAIL_REPLY_TO` placeholder to `dashboard/.env.dev.example` and `dashboard/.env.prod.example`

## 2. Email Implementation

- [x] 2.1 Add `reply_to=[settings.EMAIL_REPLY_TO]` to the `EmailMultiAlternatives` call in `_send_email` (`dashboard/utils/email.py`)

## 3. Tests

- [x] 3.1 Add test asserting confirmation email carries the Reply-To header
- [x] 3.2 Add tests asserting gift recipient and gift buyer emails carry the Reply-To header
- [x] 3.3 Add test asserting a custom `EMAIL_REPLY_TO` override is honored