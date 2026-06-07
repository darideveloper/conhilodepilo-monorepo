## Context

The booking platform currently treats `client_name` and `client_email` as both the buyer and the service recipient — they are always the same person. Gift buyers must book in their own name and manually coordinate with the recipient, creating confusion in the dashboard and no clear communication to either party.

The existing architecture is a Django backend (DRF) with an Astro+React multi-step booking form, PostgreSQL database, Stripe payments, Google Calendar sync, and Django SMTP email. The booking flow has 3 steps: service selection → calendar/time picker → form submission. Email is triggered on CONFIRMED (post-paid) or PAID (pre-paid via Stripe webhook).

## Goals / Non-Goals

**Goals:**
- Allow buyers to mark a booking as a gift and provide recipient name/email
- Always store `client_name` / `client_email` as the final service recipient (buyer if not gift, recipient if gift)
- Persist `buyer_name` / `buyer_email` on every booking for audit and communication
- Send dual role-specific emails for gift bookings (buyer gets confirmation, recipient gets notification)
- Display gift badge and buyer/recipient info in the Django admin dashboard
- Backward-compatible: existing API clients that omit gift fields get correct defaults
- Migrate existing bookings: `buyer_name` and `buyer_email` populated from `client_name` / `client_email`

**Non-Goals:**
- Gift cards, vouchers, or partial payments by third parties
- Referral or loyalty programs
- Multi-recipient bookings (one buyer gifting to multiple people in one booking)
- Custom gift messages or scheduled delivery dates
- Recipient phone number collection (buyer's phone stored for contact)

## Decisions

### D1: `client_name`/`client_email` = service recipient (not buyer)

**Decision:** `Booking.client_name` and `client_email` always represent the person receiving the service. New fields `buyer_name` and `buyer_email` store the form submitter.

**Rationale:** The dashboard is the primary operational tool — staff need to know who will show up for the appointment. `client_name` is what appears in list views, search, and Google Calendar events. Keeping it as the recipient means zero dashboard changes needed for basic display. The buyer info is supplementary, viewable in the detail form.

**Alternative considered:** Store buyer as `client_name` and recipient in gift-specific fields. Rejected because it would require changing every dashboard view, search, and calendar event to display the correct person.

### D2: Dual email via single function, not two separate template files

**Decision:** A single `send_gift_confirmation_emails(booking)` function that calls `send_role_specific_email(booking, role)` twice (once per role). The existing `send_confirmation_email` is unchanged for non-gift flow.

**Rationale:** Gift and non-gift flows diverge enough (subject line, greeting, body copy, number of recipients) that conditionals in one function would be messy. A dedicated function for gift keeps each code path clean. The email template uses a single HTML file with `{{ role }}` conditional blocks to switch greeting and body sections while sharing the services/pricing/date layout.

**Alternative considered:** Single function with `is_gift` flag and loop. Rejected because it complicates the non-gift path (80% of bookings) with gift-specific branching, making the hot path harder to read.

### D3: Recipient fields stored as `recipient_name`/`recipient_email` even though they duplicate `client_name`/`client_email`

**Decision:** Store redundant `recipient_name` and `recipient_email` fields that mirror `client_name` / `client_email` for gift bookings.

**Rationale:** `client_name` semantics change based on `is_gift` — it's the recipient for gifts and the buyer otherwise. Having explicit `recipient_*` fields makes queries and email logic unambiguous without checking `is_gift`. The data migration for existing records sets `recipient_*` to null (not needed since `client_name` is the client). Storage cost is negligible.

### D4: Frontend sends mapped field names, not raw model fields

**Decision:** The booking form's `handleSubmit` maps frontend state to API payload at submission time: when `isGift=true`, `clientName` = gift target name, and `buyerName` = form filler name. The API receives the final mapped payload directly.

**Rationale:** The frontend form always collects buyer name/email in the top fields. The "recipient" fields only appear conditionally. Mapping at submit time keeps the Zustand store schema simple (just `isGift`, `giftTargetName`, `giftTargetEmail` added) and avoids renaming existing store fields.

### D5: Stripe webhook uses booking model data, not event metadata

**Decision:** The Stripe webhook handler reads `booking.is_gift` and booking fields from the database to determine whether to send one or two emails. No additional metadata is needed in the Stripe Checkout session beyond `booking_id`.

**Rationale:** The booking is already created (with all gift fields populated) before the Stripe redirect. The webhook only transitions `PENDING` → `PAID` and triggers emails. Reading gift status from the existing booking avoids coupling Stripe metadata shape to the gift feature.

## Risks / Trade-offs

- **[Risk] Dual email sending could cause partial failure**: Buyer email succeeds but recipient email fails (or vice versa).
  → **Mitigation**: Each email is sent in a separate try/except with logging. Failure of one does not block the other.

- **[Risk] Google Calendar event description shows wrong person**: Calendar events currently reference `client_name`. For gift bookings, this correctly shows the recipient. But the description should also mention the buyer for staff context.
  → **Mitigation**: Update `sync_booking_to_google` to include `buyer_name` in the event description when `is_gift=True`.

- **[Risk] Buyer confusion from success page**: The Stripe success page says "Hemos enviado los detalles a tu correo electrónico." For gift bookings, the details went to the recipient's email, not the buyer's.
  → **Mitigation**: Update the success page copy to clarify who received what.

- **[Risk] Existing API clients break if they validate response shape**: New fields in the response (`is_gift`, `buyer_name`, `buyer_email`) could cause validation failures for strict API clients.
  → **Mitigation**: Gift fields are only present when `is_gift=True`. Non-gift responses are identical to the pre-gift format. This was already chosen in the API spec.

- **[Trade-off] Slightly more complex form logic**: The conditional gift fields add visual complexity to step 3. The animation/transition states need to feel smooth.
  → **Acceptable**: This is a standard progressive disclosure pattern.

## Open Questions

- Should the recipient phone number be collected? (Useful for the clinic to contact the actual person. If yes, adds another field.)
- Should the buyer receive a second reminder email closer to the appointment date, or only the recipient?
