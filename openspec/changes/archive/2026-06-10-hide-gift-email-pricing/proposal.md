## Why

When a booking is purchased as a gift, the recipient email currently shows the full pricing breakdown (per-service subtotals, discount, and total). This is socially awkward — gift recipients shouldn't see how much was paid. The buyer email should still show prices since they paid for it.

## What Changes

- Gift recipient email (`is_gift=True, email_role="recipient"`) will no longer show:
  - The "Subtotal" column header in the services table
  - Per-service subtotal amounts in each row
  - The pricing summary section (subtotal, discount, total rows)
- Gift buyer email (`is_gift=True, email_role="buyer"`) is **unaffected** — continues to show full pricing
- Regular booking emails (`is_gift=False`) are **unaffected** — continue to show full pricing
- The plain-text email body will also exclude pricing for gift recipients

## Capabilities

### New Capabilities

None — this is a behavioral change to existing email rendering, not a new capability.

### Modified Capabilities

None — no spec-level requirement changes. This is an implementation detail of the existing confirmation email.

## Impact

- `dashboard/utils/email.py` — add `show_pricing` context flag for each email type
- `dashboard/project/templates/email/booking_confirmation.html` — conditionally render pricing elements based on `show_pricing`
- `dashboard/booking/tests_email.py` — update gift email tests to verify prices are hidden in recipient email and present in buyer email
