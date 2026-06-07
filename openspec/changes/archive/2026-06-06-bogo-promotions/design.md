## Context

The booking platform currently uses a strictly linear pricing model: each `Event` (service) has a single `price`, and a booking's total is `SUM(event.price for each selected service)`. Services can only be added once to a booking (duplicates are prevented). The frontend never displays prices. Stripe receives a single line item with the raw total.

The business needs "Buy X Get Y Free" promotions (e.g., "Buy 3 eyebrow threadings, get 1 free") configurable per service from the Django admin. This requires changes across the full stack: data model, API contract, price calculation, admin UI, and frontend cart/summary.

### Current Architecture

- **Backend**: Django 5.2 + DRF, PostgreSQL, django-solo (CompanyProfile singleton), Unfold admin
- **Frontend (Booking)**: Astro 5 SSR + React 19, Zustand state management, no price display currently
- **Payments**: Stripe Checkout Sessions with a single line item
- **Calendar Sync**: Google Calendar integration
- **Booking Model**: `services = ManyToManyField(Event)` with auto-generated through table

### Key Constraints

- Django's default M2M through table uses an auto-increment PK with a **unique constraint on `(booking_id, event_id)`** — duplicate entries are **NOT** allowed at the ORM level. `booking.services.set([a, a, a])` silently deduplicates to a single relation.
- The current API accepts `service_ids: [1, 2]` (flat ID array) — no quantity concept
- Duration must always reflect total service quantity (promotions don't reduce appointment time)
- The availability engine (`utils/availability.py`) computes `total_duration` from the unique list of services — must be updated for quantity-aware duration

## Goals / Non-Goals

**Goals:**
- Allow admins to configure BOGO threshold promotions per service
- Support quantity > 1 for the same service in a single booking
- Calculate and persist promotional discounts
- Persist historical pricing snapshots so admin/payment records remain accurate after service price changes
- Display promotion info in the frontend
- Pass discounted total to Stripe
- Correctly compute appointment duration using quantity

**Non-Goals:**
- Promotion codes / coupon codes (separate feature)
- Percentage-based discounts (future scope)
- Time-limited promotions (activation/deactivation dates)
- Promotion stacking across different services (each service's promo is independent)
- Partial cancellation / refund logic for promotional bookings
- Modifying the Google Calendar event structure beyond price display
- Multi-currency or tax calculation changes
- Backward compatibility for the old `service_ids` API format

## Decisions

### D1: Promotion fields on Event model (not a separate model)

**Decision**: Add `buy_x` and `get_y_free` directly to `Event`.

**Alternatives considered**:
- **Separate `Promotion` model (FK to Event)**: More flexible for future promo types, but adds unnecessary complexity for a single BOGO pattern. Would require a new admin section, serializers, and API changes just to manage one promotion per service.
- **CompanyProfile-level defaults with per-service overrides**: More complex with two levels of config. The business only needs per-service control.

**Rationale**: A beauty salon typically has one active promotion per service at a time. Two fields on `Event` are sufficient, simple to query, and trivial to expose in the admin and API. If multi-promo or conditional promotions are needed later, a separate model can be introduced without breaking this schema.

### D2: Custom through model with quantity field (not duplicate M2M rows)

**Decision**: Create a `BookingServiceThrough` model with `booking`, `event`, `quantity`, and `unit_price` fields. Change `Booking.services` to use `through='BookingServiceThrough'`.

**Alternatives considered**:
- **Duplicate M2M rows**: REJECTED. Django's default M2M through table has a unique constraint on `(booking_id, event_id)`. Using `booking.services.set([a, a, a])` silently deduplicates to a single entry. Bulk-creating duplicate rows through the raw through model would bypass the ORM, break admin inlines, and make queries fragile. This approach does not work.
- **JSON field on Booking storing quantities**: Loses referential integrity, can't use M2M queries, harder to join/filter.

**Rationale**: A custom through model with `quantity` is the correct Django pattern for M2M relationships with extra data. It preserves referential integrity, works with the ORM, makes all queries explicit (`item.quantity * item.unit_price`), and cleanly handles the quantity concept throughout the codebase. `unit_price` snapshots the service price at booking time.

**Model details**:
- `BookingServiceThrough.booking`: `ForeignKey(Booking, related_name="booking_services", on_delete=CASCADE)`
- `BookingServiceThrough.event`: `ForeignKey(Event, related_name="booking_services", on_delete=CASCADE)`
- `BookingServiceThrough.quantity`: `PositiveIntegerField(default=1)`
- `BookingServiceThrough.unit_price`: `DecimalField(max_digits=10, decimal_places=2)` set from `Event.price` at booking creation
- Unique constraint on `(booking, event)`

**Impact on existing code**: All code that uses `booking.services.all()` must be updated:
- `Booking.calculate_end_time()` — must use through model with quantity
- `signals.py` (`m2m_changed` handler) — must use through model with quantity
- `admin.py` (BookingAdmin.get_price, get_services, BookingInline) — must use through model
- `google_calendar.py` (booking_to_event_body) — must use through model
- `views.py` (CreateBookingView) — must use through model

### D3: Persist pricing snapshots on Booking and BookingServiceThrough

**Decision**: Store `unit_price` on each `BookingServiceThrough` row, plus `original_amount`, `discount_amount`, and `total_amount` on `Booking` at creation time.

**Rationale**: Service prices and promotions may change after booking. Persisting only `discount_amount` is insufficient because recomputing `SUM(quantity * Event.price)` would use current service prices. Snapshotting `unit_price`, `original_amount`, `discount_amount`, and `total_amount` ensures historical accuracy for admin reporting, Stripe reconciliation, Google Calendar descriptions, and future refund analysis.

### D4: Threshold-style BOGO formula

**Decision**: `free_count = (qty // buy_x) * get_y_free`, capped at `qty`. Paid count = `qty - free_count`.

**Rationale**: This matches the user's requirement. "Buy 2 Get 1 Free" means every 2 purchased earns 1 free. The formula stacks: 2 purchases → 1 free, 4 purchases → 2 free, etc.

### D5: Breaking API change — new input format

**Decision**: Change `POST /api/bookings/` from `service_ids: [1, 2]` to `services: [{service_id: 1, quantity: 3}, {service_id: 2, quantity: 1}]`.

**Alternatives considered**:
- **Expand flat `service_ids` with duplicates**: Sending `[1, 1, 1, 2]` is fragile, hard to validate, and confusing.
- **Keep `service_ids` and add a separate `quantities` mapping**: More complex for both frontend and backend.

**Rationale**: The new format is explicit, self-documenting, and easy to validate. The booking frontend is the only consumer of this endpoint (not a public API with external clients), so a breaking change is acceptable.

### D6: Single Stripe line item with discounted total

**Decision**: Continue sending a single line item to Stripe with the discounted total amount. No line-item breakdown per service or per discount.

**Rationale**: The current Stripe integration uses a single line item. Adding itemized breakdowns would require significant changes to `stripe_utils.py` and the Stripe session creation. A single total is simpler and matches the current UX (the user sees a total charge, not itemized). Promotion details are visible in the Booking admin and Google Calendar description.

### D6.1: Zero-total PRE-PAID bookings skip Stripe

**Decision**: If a booking includes PRE-PAID services but the discounted `total_amount <= 0`, the backend SHALL NOT create a Stripe Checkout Session. The booking should be completed internally with no external payment requirement.

**Rationale**: Stripe payment-mode Checkout is not appropriate for zero-amount payments. A zero-total booking should behave like a confirmed no-payment booking while preserving the pricing snapshot (`original_amount`, `discount_amount`, `total_amount=0`).

### D7: Frontend price calculation (client-side)

**Decision**: Frontend computes subtotal, discount, and total locally from the service data and quantities in the Zustand store. No separate server-side "price calculation" endpoint.

**Rationale**: The promotion rules (`buy_x`, `get_y_free`) and prices are already sent to the frontend via `/api/services/`. The formulas are simple integer arithmetic. A round-trip for price calculation would add latency and complexity for no benefit. The server independently validates and computes the discount at booking creation time.

### D8: Availability endpoints accept quantities for duration

**Decision**: The availability API endpoints (`/api/availability/days/` and `/api/availability/slots/`) will accept an optional `quantities` parameter alongside `service_ids`. When provided, `total_duration` is computed as `SUM(service.duration_minutes * quantity)` instead of `SUM(service.duration_minutes)`.

**Rationale**: When a user books Service A × 3, the appointment needs 3× the duration. The availability engine must find time slots that accommodate the full duration. The `service_ids` parameter remains deduplicated (unique IDs), and `quantities` is a parallel array of the same length specifying how many of each service. This avoids sending duplicate IDs while still communicating durations correctly.

**Validation**:
- If `quantities` is omitted, all quantities default to 1.
- If provided, `quantities` length MUST match `service_ids` length.
- Every quantity MUST be a positive integer.
- Invalid `quantities` MUST return HTTP 400.

### D9: Through-model persistence and Google sync ordering

**Decision**: Booking creation SHALL calculate pricing and duration before creating the booking, create the booking with stored pricing fields, create `BookingServiceThrough` rows in the same transaction, then schedule Google sync/email only after transaction commit. Existing `m2m_changed` behavior should be removed or replaced with through-model-specific `post_save`/`post_delete` logic that recalculates `end_time` once and avoids duplicate sync.

**Rationale**: The current code creates a booking and then sets M2M services. With a custom through model, booking services must exist before Google Calendar descriptions, duration, and price display are correct. Syncing before through rows exist would produce incomplete calendar events.

## Risks / Trade-offs

**[Risk] Service prices change between frontend display and booking submission** → The backend snapshots `unit_price`, `original_amount`, `discount_amount`, and `total_amount` from current database values at submission time. Minor UX discrepancy is possible if admin changes prices mid-booking, but persisted booking records and Stripe totals remain internally consistent.

**[Risk] Custom through model increases migration complexity** → The migration must: (1) create `BookingServiceThrough`, (2) migrate existing M2M rows from the auto-generated table, (3) update the `Booking.services` field to use the new through model, (4) drop the old auto-generated table. This is a well-understood Django pattern but requires a multi-step migration. Test thoroughly on a staging database before production.

**[Risk] Django may not auto-generate a safe through-model migration** → Use an explicit staged migration, likely with `SeparateDatabaseAndState` or separate schema/data migrations. Verify on a database with existing bookings before implementation is marked complete.

**[Risk] Breaking API change affects any other consumers** → The booking frontend is the only consumer. The API is not documented for external use. This is acceptable.

**[Risk] Refund calculations for promotional bookings** → If a user cancels part of a promotional booking, Stripe refund handling would need manual proration. This is explicitly out of scope (Non-Goal).

**[Risk] `get_y_free > buy_x` creates extreme discounts** → An admin could configure `buy_x=1, get_y_free=10`, making most units free. This may be intentional, so do not block it by default. Use help text or non-blocking admin messaging rather than a hard `ValidationError` unless the business later requests strict validation.

**[Risk] Availability duration miscalculation if quantities not sent** → If the frontend upgrade is deployed separately from the backend and sends requests without `quantities`, the availability engine will compute duration for quantity=1. This is safe (under-estimates slot size) but may show slots that are too short. Default `quantity` to 1 when not provided.

## Migration Plan

1. Create `BookingServiceThrough` model with `booking`, `event`, `quantity`, and `unit_price` fields plus explicit related names
2. Add `buy_x`, `get_y_free` to `Event`; add `original_amount`, `discount_amount`, and `total_amount` to `Booking`
3. Create data migration to copy existing M2M rows from auto-generated `booking_booking_services` table into `BookingServiceThrough` (with `quantity=1`)
4. Update `Booking.services` field to use `through='BookingServiceThrough'`, using an explicit migration strategy (`SeparateDatabaseAndState` or staged migrations) if Django cannot safely auto-generate the transition
5. Update all code that accesses `booking.services.all()` to use the through model
6. Deploy backend changes (new fields, through model, updated views) — availability endpoints default `quantities` to 1 if not provided for backward compatibility
7. Deploy frontend changes — new quantity UI, price display, new API format, quantities in availability calls
8. Remove backward compatibility for `service_ids` after frontend is deployed

### Rollback
- Migrations can be reversed only if the staged through-model migration is written with an explicit reverse path
- The M2M data migration (step 3) must be tested with a backup
- Frontend can be rolled back independently
- No data integrity risk — new fields have defaults, existing M2M data is preserved
