## Why

The booking system currently has a strictly linear pricing model — every service is charged at its listed price, regardless of quantity. This prevents the business from running "Buy X, Get Y Free" volume promotions that are standard in the beauty industry (e.g., "Buy 3 eyebrow threadings, get 1 free"). These promotions are a key competitive lever and must be configurable directly from the admin panel (Django admin) without code deployments.

## What Changes

- **BREAKING** `POST /api/bookings/` input format changes from `service_ids: [int]` to `services: [{service_id, quantity}]` to support multiple quantities of the same service
- New `BookingServiceThrough` custom M2M through model with `quantity`, `unit_price`, and explicit related names, replacing the auto-generated through table
- `Event` model gains `buy_x` (threshold) and `get_y_free` (free per threshold) fields
- `Booking` model gains `original_amount`, `discount_amount`, and `total_amount` fields to persist a historical pricing snapshot
- A `calculate_service_discount()` utility implements threshold-style BOGO pricing
- Admin UI (`EventAdmin`) exposes promotion fields per service
- Booking admin shows discount, quantity-aware service names, and through-model inline
- Frontend booking store, service selection, and summary form become price-aware and display promotion info
- Google Calendar sync description shows discounted amount and quantity-aware service names
- Stripe receives a single line item with the discounted total
- Zero-total PRE-PAID bookings bypass Stripe and complete internally
- Availability endpoints accept quantities for duration-weighted slot calculation
- Availability endpoints validate `quantities` length and positivity when provided
- All code referencing `booking.services.all()` updated to use through model with quantity

## Capabilities

### New Capabilities
- `pricing-promotions`: BOGO threshold pricing model — configurable per-service from Django admin, applied at booking creation, displayed in frontend cart and confirmation

### Modified Capabilities
- `dashboard-models`: Event and Booking models gain promotion/price snapshot fields; new BookingServiceThrough through model replaces auto-generated M2M table
- `booking-ui`: Frontend cart gains quantity selectors, price display with promotion breakdown, and quantity-aware availability requests
- `config-api`: Services API response includes promotion fields (`buy_x`, `get_y_free`); availability endpoints accept quantities
- `payment-flow`: Stripe checkout total calculated after discount using through-model quantities; zero-total bookings skip Stripe
- `db-migration`: New migration for model changes including through-model data migration
- `api-contracts`: Booking creation endpoint contract changes; availability endpoints accept quantities

## Impact

- **Django backend**: `booking/models.py` (new BookingServiceThrough, Event + Booking pricing fields), `booking/views.py` (CreateBookingView + availability views), `booking/serializers.py` (expose promo fields), `booking/admin.py` (EventAdmin + BookingAdmin + through inline), `booking/signals.py` (replace M2M sync path with quantity-aware through-model behavior), `utils/pricing.py` (new), `utils/availability.py` (quantity-aware duration), `utils/google_calendar.py` (quantity-aware names/prices), `utils/stripe_utils.py` (caller passes discounted amount)
- **New migration**: Multi-step migration creating through model, migrating existing data, adding price snapshot fields, and changing Django model state safely
- **Stripe**: `stripe_utils.py` unchanged structurally, but caller passes discounted total
- **Frontend (booking)**: Store, service selection, booking form, availability API calls — all touched
- **Booking API contract**: Breaking change to POST /api/bookings/ input format
- **Availability API**: New optional `quantities` parameter for duration calculation
