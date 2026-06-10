## Context

The booking confirmation email system uses a single HTML template (`booking_confirmation.html`) and a plain-text builder (`_build_plain_text()`) for all email types. Currently, all recipients — regular clients, gift recipients, and gift buyers — receive identical pricing data in full detail (per-service subtotals, discount, total).

There is no concept of guest vs registered users. The only distinction is `is_gift` (boolean) and `email_role` ("recipient" or "buyer") on the context passed to the template.

The gift recipient currently sees the same pricing breakdown as the buyer, which is inappropriate — a gift recipient shouldn't know how much was paid.

## Goals / Non-Goals

**Goals:**
- Hide all pricing information from the gift recipient email (`email_role="recipient"`)
- Keep full pricing in the gift buyer email (`email_role="buyer"`)
- Keep full pricing in regular (non-gift) booking emails
- Handle both HTML and plain-text fallback

**Non-Goals:**
- No new email templates (keep using the single shared template)
- No database schema changes
- No new configuration or environment variables
- No changes to the booking creation flow or API
- No logging or audit trail for price hiding

## Decisions

### Decision 1: Context flag `show_pricing` over `email_role` checks in template

**Option B (chosen):** Add a `show_pricing` boolean to the context in `email.py`. The three call sites set it explicitly:
- `send_confirmation_email()` → `show_pricing=True`
- `send_gift_confirmation_emails()` recipient → `show_pricing=False`
- `send_gift_confirmation_emails()` buyer → `show_pricing=True`

The template checks `{% if show_pricing %}` around pricing elements.

**Option A rejected:** Checking `{% if not is_gift or email_role == "buyer" %}` directly in the template. More complex condition, couples template logic to role semantics, harder to test, harder to change later.

**Option C rejected:** Creating a separate template for gift recipients. Duplicates ~140 lines of HTML, harder to maintain consistency.

### Decision 2: Conditional rendering approach in template

The services table has 4 columns: Servicio | Cant. | Duración | Subtotal. For gift recipients, the Subtotal column is removed entirely (header + data cells), leaving a clean 3-column service list.

The entire pricing summary block (subtotal/discount/total rows) is wrapped in `{% if show_pricing %}`.

No `colspan` adjustments needed — the cells simply aren't emitted.

### Decision 3: Plain-text fallback

The `_build_plain_text()` function also receives `show_pricing` and skips per-service prices and the subtotal/discount/total summary when `False`.

## Risks / Trade-offs

- **[Low] Template regression:** The same template serves all three email types. A bug in the conditional could accidentally expose prices to recipients or hide them from buyers. **Mitigation:** Tests explicitly check price presence per email role.
- **[Low] Services table visual imbalance:** Removing the Subtotal column leaves a 3-column table. At typical service name lengths this looks fine. **Mitigation:** No action needed unless QA flags it.
- **[None] Data exposure:** No security concern — prices are already client-side data. This is a UX/social choice.
