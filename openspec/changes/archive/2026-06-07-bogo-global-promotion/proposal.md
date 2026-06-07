## Why

The initial BOGO implementation stored promotion thresholds (`buy_x`, `get_y_free`) per-service on the `Event` model. For a small beauty salon running a single global promotion ("Buy 2 Get 1 Free on everything"), this adds unnecessary configuration overhead and complexity. Additionally, the customer confirmation email does not display quantities, prices, or promotional discounts — it just lists service names with no pricing info.

## What Changes

- **BREAKING** BOGO promotion fields (`buy_x`, `get_y_free`) move from per-service (`Event`) to global (`CompanyProfile`). The `/api/services/` endpoint no longer returns these fields per service.
- **BREAKING** The `/api/config/` endpoint now returns `buy_x` and `get_y_free` at the global level.
- Promotion becomes all-or-nothing: every service is equally eligible. No per-service opt-out.
- A new migration (`0017`) removes `buy_x`/`get_y_free` from `Event` and adds them to `CompanyProfile`. Existing per-service values are discarded.
- `calculate_service_discount()` becomes a pure function: `(unit_price, quantity, buy_x, get_y_free)` — no ORM dependency.
- Customer confirmation email updated to show quantity per service (`Service × N`), subtotal per line, discount breakdown, and final total.
- Promotion badge ("Buy X Get Y Free") visible on all frontend steps (service selection, booking form, success confirmation), not just Step 1.
- Frontend reads promotion config from the global config endpoint instead of per-service API data.
- **Bug fix**: Frontend discount calculation guard changed from `qty > buy_x` to `qty >= buy_x` so exact-threshold quantities (e.g., qty=2 with Buy 2 Get 1 Free) correctly show the discount.
- **Bug fix**: `BookingFlow.tsx` pre-selected service from URL parameters lacked `quantity: 1`, causing `NaN` in the cart counter. Fixed by adding `quantity: 1` to the initial selection.
- **i18n**: Admin Promotions section labels translated to Spanish via `.po` file. Frontend `Discount` label wired to translation system (`t.form.discount`).
- **Dev tool**: New Django management command `test_email.py` to send test confirmation emails without real bookings or Stripe payments.

## Capabilities

### New Capabilities
*(none — this is a refactor of existing capabilities)*

### Modified Capabilities
- `dashboard-models`: Promotion fields move from `Event` to `CompanyProfile`; `Event` loses `buy_x`/`get_y_free`
- `config-api`: Config API now returns global `buy_x`/`get_y_free`; services API no longer returns per-service promotion fields
- `booking-ui`: Frontend reads promotion from global config instead of per-service data; badge shown on all steps
- `db-migration`: New migration removes fields from Event and adds to CompanyProfile
- `confirmation-email`: Email now includes quantity, unit price, subtotal, discount breakdown, and total for each service

## Impact

- **Django backend** (`booking/models.py`): Remove `buy_x`/`get_y_free` from Event; add to CompanyProfile
- **Pricing utility** (`utils/pricing.py`): `calculate_service_discount` becomes pure function with signature `(unit_price, quantity, buy_x, get_y_free)`
- **Views** (`booking/views.py`): CreateBookingView reads BOGO config from CompanyProfile instead of Event
- **Serializers** (`booking/serializers.py`): Remove promotion fields from EventSerializer; add to CompanyProfileSerializer
- **Admin** (`booking/admin.py`): Remove promotion fields from EventAdmin; add to CompanyProfileAdmin
- **Migration**: New `0017` migration — AddField to CompanyProfile, RemoveField from Event
- **Frontend** (`booking/`): Remove `buy_x`/`get_y_free` from `DashboardService` type; read from `AppConfig` instead; update `getServicePromotion()` and `priceSummary` to use config; show badge on all steps
- **Email** (`utils/email.py` + `booking_confirmation.html`): Use `booking.booking_services.all()` with quantities; render price summary table with discount
- **Tests**: `tests_pricing.py` refactored for pure function; `tests_bogo.py` updated for global config; `tests_email.py` updated for new context shape
- **i18n**: Spanish translations added to `locale/es/LC_MESSAGES/django.po` for new admin labels and help texts
- **Frontend i18n**: Hardcoded `"Discount"` labels in `BookingForm.tsx` replaced with `t.form.discount` translation key
- **Dev tool**: New management command `booking/management/commands/test_email.py` for ad-hoc email testing with terminal-prompt, env var, or direct argument

## File Changes Summary

| File | Change |
|------|--------|
| `booking/models.py` | Added `buy_x`/`get_y_free` to `CompanyProfile`; removed from `Event` |
| `booking/migrations/0017_*.py` | New migration |
| `utils/pricing.py` | Pure function `(unit_price, qty, buy_x, get_y_free)` |
| `booking/views.py` | `CreateBookingView` reads from `CompanyProfile` |
| `booking/serializers.py` | Updated both serializers |
| `booking/admin.py` | Promotions fieldset on `CompanyProfileAdmin` |
| `utils/email.py` | Through-model query, pricing context |
| `project/templates/email/booking_confirmation.html` | Quantity column, price summary table |
| `booking/src/store/useBookingStore.ts` | `buy_x`/`get_y_free` on `AppConfig` |
| `booking/src/lib/api/endpoints/services.ts` | Removed from `DashboardService` |
| `booking/src/components/organisms/BookingServiceSelection.tsx` | Reads from config |
| `booking/src/components/organisms/BookingForm.tsx` | Reads from config; `>=` fix; badge on all steps; `Discount` → `t.form.discount` |
| `booking/src/components/organisms/BookingFlow.tsx` | Added `quantity: 1` to URL pre-selection |
| `booking/tests_pricing.py` | Pure function tests |
| `booking/tests_bogo.py` | Global config tests + config endpoint test |
| `booking/tests_email.py` | Quantity/pricing assertions |
| `locale/es/LC_MESSAGES/django.po` | Spanish translations for Promotions section |
| `booking/management/commands/test_email.py` | New dev tool |
| `scripts/test_email.py` | Removed (replaced by management command) |
