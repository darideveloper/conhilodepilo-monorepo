## 1. Add `show_pricing` context flag to email functions

- [x] 1.1 In `send_confirmation_email()`: set `show_pricing=True` in context update
- [x] 1.2 In `send_gift_confirmation_emails()` recipient block: set `show_pricing=False`
- [x] 1.3 In `send_gift_confirmation_emails()` buyer block: set `show_pricing=True`

## 2. Hide pricing in HTML template

- [x] 2.1 Conditionally render "Subtotal" `<th>` in services table header based on `show_pricing`
- [x] 2.2 Conditionally render per-service subtotal `<td>` in each row based on `show_pricing`
- [x] 2.3 Wrap entire pricing summary block (subtotal/discount/total rows) in `{% if show_pricing %}`

## 3. Hide pricing in plain-text fallback

- [x] 3.1 Pass `show_pricing` through `_build_plain_text()` via context
- [x] 3.2 Skip per-service price info when `show_pricing` is `False`
- [x] 3.3 Skip subtotal/discount/total summary when `show_pricing` is `False`

## 4. Update tests

- [x] 4.1 Add assertions that gift recipient email body (HTML + plain-text) does NOT contain prices
- [x] 4.2 Add assertions that gift buyer email body (HTML + plain-text) DOES contain prices
- [x] 4.3 Verify regular booking email is unaffected (existing tests pass unchanged)

## 5. Verify all existing tests still pass

- [x] 5.1 Run the email test suite: `python manage.py test booking.tests_email`
