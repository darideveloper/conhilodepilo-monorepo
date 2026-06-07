## Context

The BOGO promotion system was initially implemented with `buy_x` and `get_y_free` fields on each `Event` (service) record via migration `0016`. This allowed per-service promotion configuration. However, the business runs a single global promotion ("Buy 2 Get 1 Free on everything"), making per-service configuration unnecessary overhead. The admin must set the same values on every service, which is error-prone.

Additionally, the customer confirmation email (`utils/email.py`) was never updated to reflect the new pricing model — it still uses `booking.services.all()` which returns Event objects without quantity or pricing info. The email shows just service names with no quantities, prices, or discount breakdown.

### Current State

```
┌────────────────────┐     ┌─────────────────────┐
│      Event         │     │   CompanyProfile    │
│  buy_x: 2          │     │  (no promotion      │
│  get_y_free: 1     │     │   fields)           │
│  price: 30.00      │     └─────────────────────┘
└────────┬───────────┘              │
         │ per-service              │ global config
         ▼                          ▼
  ┌──────────────────────────────────────┐
  │          Frontend                    │
  │  reads buy_x/get_y_free per-service  │
  │  badge only on Step 1               │
  │  BUG: qty > buy_x (not >=)          │
  └──────────────────────────────────────┘

  Email: booking.services.all() → no quantities, no prices, no discount
```

### Key Constraints

- Migration `0016` is already deployed — `Event` has `buy_x`/`get_y_free` columns
- `BookingServiceThrough` already exists with `quantity` and `unit_price`
- `Booking` already has `original_amount`, `discount_amount`, `total_amount`
- The pricing snapshot flow already works at the backend level
- Frontend currently computes discounts locally from per-service `buy_x`/`get_y_free`

## Goals / Non-Goals

**Goals:**
- Move BOGO config from per-service (`Event`) to global (`CompanyProfile`)
- Keep the same pricing formula, just read from a different source
- Update email notification to render quantities, prices, and discount breakdown
- Show promotion badge on all frontend steps
- Fix the frontend discount calculation bug (`qty > buy_x` → `qty >= buy_x`)
- Refactor `calculate_service_discount()` to a pure function with no ORM dependency

**Non-Goals:**
- Per-service promotion opt-out (`exclude_from_promotion` flag)
- Percentage-based discounts (separate feature)
- Time-limited promotions (activation/deactivation dates)
- Promotion stacking across services
- Partial cancellation / refund logic
- Max quantity validation (handled naturally by availability engine)
- Frontend tests (will rely on existing manual test tasks)

## Decisions

### D1: BOGO config moves to CompanyProfile (global singleton)

**Decision**: Add `buy_x` and `get_y_free` to `CompanyProfile`. Remove them from `Event`.

**Rationale**: The business runs one promotion across all services. A singleton model is the simplest place to store this. `CompanyProfile` is already the central config hub and is fetched by the frontend via `/api/config/`.

**Model changes**:
```python
# CompanyProfile gets:
buy_x = models.PositiveIntegerField(_("Buy X"), default=0,
    help_text=_("Buy X items to trigger promotion. Set to 0 to disable."))
get_y_free = models.PositiveIntegerField(_("Get Y Free"), default=0,
    help_text=_("Free items per threshold. Set to 0 to disable."))

# Event loses:
# buy_x (remove)
# get_y_free (remove)
```

### D2: Pure function for discount calculation

**Decision**: `calculate_service_discount(unit_price, quantity, buy_x, get_y_free)` — pure function with no ORM dependency.

```python
def calculate_service_discount(unit_price, quantity, buy_x, get_y_free):
    if buy_x <= 0 or get_y_free <= 0 or quantity <= 0:
        return Decimal('0.00'), 0
    free_count = min((quantity // buy_x) * get_y_free, quantity)
    discount_amount = Decimal(str(free_count)) * unit_price
    return discount_amount, free_count
```

**Rationale**: Removing the ORM dependency makes the function trivially testable (no fixtures needed), usable from the frontend, and its contract is explicit.

**Impact**: `calculate_booking_totals()` also needs to accept `buy_x`/`get_y_free` params. Views.py reads them from `CompanyProfile.get_solo()` and passes them through.

### D3: Email notification uses through-model with quantities

**Decision**: Replace `booking.services.all()` with `booking.booking_services.select_related('event').all()` and build service list entries with quantity, unit_price, subtotal, and duration.

**Rationale**: The through model already stores `quantity` and `unit_price` at booking time. Using it directly gives accurate per-line data without re-querying Event prices (which may have changed).

**Email template changes**:
```
  ┌─────────────────────┬─────┬──────────┬──────────┐
  │ Servicio            │Cat. │ Duración │ Subtotal │
  ├─────────────────────┼─────┼──────────┼──────────┤
  │ Eyebrow Threading   │  3  │  90 min  │  €90.00  │
  │ Facial              │  1  │  45 min  │  €45.00  │
  ├─────────────────────┴─────┴──────────┼──────────┤
  │ Subtotal                             │ €135.00  │
  │ Promoción (Buy 2 Get 1 Free)         │  -€30.00  │ ← if discount > 0
  │ Total                                │ €105.00  │
  └──────────────────────────────────────┴──────────┘
```

### D4: Frontend reads promotion from global config

**Decision**: Remove `buy_x`/`get_y_free` from `DashboardService` type. Read them from `AppConfig` (already fetched and stored in Zustand store).

**Rationale**: The config endpoint is already fetched on every page load. Adding two fields to it is simpler than reading per-service data. The `getServicePromotion()` function no longer needs a `serviceId` parameter — it just checks if the global config has an active promotion.

**Frontend changes**:
- `AppConfig` interface gains `buy_x: number` and `get_y_free: number`
- `DashboardService` loses `buy_x` and `get_y_free`
- `getServicePromotion()` reads from `config` instead of `service`
- `priceSummary` in `BookingForm.tsx` reads from `config` instead of `service`
- Badge rendered on all steps where selected services are displayed

### D5: Fix frontend discount condition

**Decision**: Change `qty > service.buy_x` → `qty >= config.buy_x` in the frontend `priceSummary`.

**Rationale**: The current guard `qty > service.buy_x` means exact-threshold quantities (e.g., qty=2 with Buy 2 Get 1 Free) show zero discount in the frontend preview, while the backend correctly applies the discount. This is a bug. The fix aligns frontend and backend behavior.

### D6: Promotion badge visible on all steps

**Decision**: Render the "Buy X Get Y Free" badge on service items across all booking UI steps:
- Step 1 (service selection cart) — already done
- Step 3 (booking form summary) — add next to each service name
- Success confirmation screen — show in the service list
- Email notification — include in the confirmation email text/HTML

**Rationale**: Users should see what promotion applies at every stage of the flow, from selection through confirmation.

## Risks / Trade-offs

**[Risk] Per-service BOGO values are lost on migration** → Accepted. Migration 0017 removes the columns from Event. Any services with non-default values will lose them. The admin sets the global value after deployment. No data loss for default (0,0) values.

**[Risk] Frontend and backend discount logic could diverge** → Mitigated by making the pricing formula identical in both places. The pure function design makes this trivial to verify.

**[Risk] Email contains stale prices if booking is very old** → Not an issue. Email is sent at booking creation time and uses `unit_price` snapshots from `BookingServiceThrough`, not current Event prices.

**[Risk] Global promotion may not fit future needs** → If the business later needs per-service or multi-tier promotions, the CompanyProfile fields can be kept as defaults and a separate `Promotion` model can be introduced without breaking existing code. The migration path is forward-compatible.

## Migration Plan

1. Add `buy_x`/`get_y_free` fields to `CompanyProfile` model
2. Remove `buy_x`/`get_y_free` fields from `Event` model
3. Generate migration `0017` (autodetected: AddField to CompanyProfile + RemoveField from Event)
4. Update all code that reads `Event.buy_x`/`get_y_free` to read from `CompanyProfile.get_solo()`
5. Refactor `calculate_service_discount()` to pure function
6. Update `calculate_booking_totals()` to accept global config params
7. Update `views.py` to pass global config to pricing functions
8. Update `serializers.py` — remove from EventSerializer, add to CompanyProfileSerializer
9. Update `admin.py` — remove from EventAdmin, add to CompanyProfileAdmin
10. Update `utils/email.py` and email template for quantities/prices/discounts
11. Update frontend types, components, and store
12. Fix frontend discount bug
13. Apply migration to dev database
14. Manual test: full booking flow with global promotion

### Rollback
- Migration `0017` is reversible (reverse AddField/RemoveField)
- Frontend can be rolled back independently
- Email changes are cosmetic — rollback restores old template
- No data integrity risk — pricing snapshots on Booking are unaffected
