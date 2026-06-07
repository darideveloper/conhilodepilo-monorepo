## 1. Data Model & Migration

- [x] 1.1 Create `BookingServiceThrough` model in `dashboard/booking/models.py` with fields: `booking` (FK to Booking, `related_name="booking_services"`), `event` (FK to Event, `related_name="booking_services"`), `quantity` (PositiveIntegerField, default=1), `unit_price` (DecimalField, max_digits=10, decimal_places=2), with `unique_together = ('booking', 'event')` and `verbose_name`/`verbose_name_plural` translations
- [x] 1.2 Update `Booking.services` ManyToManyField to use `through='BookingServiceThrough'`
- [x] 1.3 Add `buy_x` (PositiveIntegerField, default=0) and `get_y_free` (PositiveIntegerField, default=0) fields to the `Event` model with verbose names and help text
- [x] 1.4 Add `original_amount`, `discount_amount`, and `total_amount` (DecimalField, max_digits=10, decimal_places=2, default=Decimal('0.00')) fields to the `Booking` model
- [x] 1.5 Add admin help text for `buy_x`/`get_y_free`, including a non-blocking note that `get_y_free > buy_x` creates aggressive discounts
- [x] 1.6 Generate and review a staged Django migration — this must: (a) create `BookingServiceThrough` table, (b) add `buy_x`/`get_y_free` to Event, (c) add `original_amount`/`discount_amount`/`total_amount` to Booking, (d) migrate data from auto-generated `booking_booking_services` into `BookingServiceThrough` with `quantity=1` and `unit_price=Event.price`, (e) backfill `original_amount` and `total_amount` from migrated line items and `discount_amount=0`, (f) update `Booking.services` to use the new through model. Use `SeparateDatabaseAndState` or separate schema/data migrations if Django cannot safely auto-generate the transition.
- [ ] 1.7 Apply migration to dev database with existing bookings and verify all existing bookings have services preserved with `quantity=1`, `unit_price`, and backfilled booking totals

## 2. Pricing Utility

- [x] 2.1 Create `dashboard/utils/pricing.py` with `calculate_service_discount(service, quantity)` function implementing the threshold formula: `free_count = min((qty // buy_x) * get_y_free, qty)` returning `(discount_amount, free_count)`
- [x] 2.2 Create `calculate_booking_totals(booking_services)` function that accepts a list of `BookingServiceThrough` objects (or `(Event, quantity, unit_price)` tuples) and returns `(original_amount, discount_amount, total_amount, total_duration)` using through-model quantities and booking-time unit prices
- [x] 2.3 Add unit tests for `calculate_service_discount` covering: no promotion (buy_x=0), qty below threshold, qty at threshold, qty above threshold, stacking scenarios, edge cases (qty=0, buy_x=0, get_y_free=0, get_y_free > buy_x)

## 3. Update All Code That Uses `booking.services.all()`

- [x] 3.1 Update `Booking.calculate_end_time()` in `models.py` to use `self.booking_services.all()` with `quantity * duration_minutes` instead of `self.services.all()`
- [x] 3.2 Update `BookingInline` in `admin.py` to use `BookingServiceThrough` instead of `Booking.services.through`, showing `quantity` in the inline
- [x] 3.3 Update `BookingAdmin.get_price` to display stored `total_amount`, with original/discount context when `discount_amount > 0`
- [x] 3.4 Update `BookingAdmin.get_services` to show "Service Name × N" format using through model quantities
- [x] 3.5 Update `booking_to_event_body()` in `google_calendar.py` to use `booking.booking_services.all()` and show quantity-aware service names (e.g., "Eyebrow Threading ×3") and discounted price in description
- [x] 3.6 Update `m2m_changed` signal handler in `signals.py` to use `BookingServiceThrough` for duration calculation — note: this signal may need to be changed from `m2m_changed` to `post_save` on `BookingServiceThrough`, or recalculated differently since the through model changes how M2M signals fire
- [x] 3.7 Update `Booking.save()` method's `calculate_end_time()` call to work with the new through model — consider moving end_time calculation to happen after through-model rows are committed

## 4. Admin UI Updates

- [x] 4.1 Add `buy_x` and `get_y_free` fields to `EventAdmin.fieldsets` in `dashboard/booking/admin.py` under the "General" section with appropriate help text
- [x] 4.2 Update `BookingAdmin` to show `original_amount`, `discount_amount`, and `total_amount` in list display and detail view
- [x] 4.3 Update `BookingServiceThrough` inline in BookingAdmin to show service name, quantity, unit price, and line subtotal

## 5. API — Serializers & Views

- [x] 5.1 Add `buy_x` and `get_y_free` fields to `EventSerializer` in `dashboard/booking/serializers.py`
- [x] 5.2 Refactor `CreateBookingView.post()` in `dashboard/booking/views.py` to accept `services` as `[{service_id, quantity}]` instead of `service_ids`
- [x] 5.3 In `CreateBookingView`, create `BookingServiceThrough` rows with quantities and booking-time `unit_price` using `BookingServiceThrough.objects.bulk_create(...)` instead of `booking.services.set()`
- [x] 5.4 Calculate `original_amount`, `discount_amount`, and `total_amount` using `calculate_booking_totals()` and store them on the Booking record
- [x] 5.5 Calculate `total_duration` using quantities and set the correct `end_time` when creating the Booking
- [x] 5.6 Pass stored `total_amount` to Stripe's `create_checkout_session` for PRE-PAID bookings when `total_amount > 0`
- [x] 5.7 If a PRE-PAID booking has `total_amount <= 0`, skip Stripe Checkout and complete the booking internally with `payment_required: false`
- [x] 5.8 Include `original_amount`, `discount_amount`, and `total_amount` in the booking creation API response
- [x] 5.9 Add booking input validation: reject negative quantities, reject zero quantities, validate service_ids exist, enforce quantity ≥ 1
- [x] 5.10 Update availability views (`AvailabilityView`, `AvailabilitySlotsView`) to accept an optional `quantities` query parameter alongside `service_ids`, validate length/positive integers, and compute `total_duration` as `SUM(duration × quantity)` instead of `SUM(duration)`
- [x] 5.11 Update `utils/availability.py` functions (`get_available_dates`, `get_available_slots`) to accept and use a `quantities` dict parameter for duration calculation

## 6. Frontend — Store Changes

- [x] 6.1 Update `SelectedService` type in `booking/src/store/useBookingStore.ts` to include `quantity: number` (default=1)
- [x] 6.2 Remove the duplicate-prevention logic (`isAlreadyAdded` check) and replace with quantity-increment logic in `BookingServiceSelection.tsx`
- [x] 6.3 Add computed selector functions for: `getOriginalTotal()`, `getDiscountAmount()`, `getFinalTotal()`, per-service discount info
- [x] 6.4 Update `fetchAvailability` and `fetchSlots` calls in the store to pass quantity data alongside service IDs

## 7. Frontend — Service Selection UI

- [x] 7.1 Update `BookingServiceSelection.tsx` to display quantity +/- controls for each selected service
- [x] 7.2 Show "Buy X Get Y Free" badge next to services that have an active promotion in the dropdown/service list
- [x] 7.3 Display per-service subtotal (price × quantity) and per-service discount where applicable in the cart area

## 8. Frontend — Booking Form & Price Summary

- [x] 8.1 Add a price summary section to `BookingForm.tsx` showing: subtotal, discount line (if applicable), and total
- [x] 8.2 Localize the discount label (e.g., "Buy 2 Get 1 Free" in the user's language)
- [x] 8.3 Display formatted prices using the currency from `AppConfig.currency`

## 9. Frontend — API Client Update

- [x] 9.1 Update `booking/src/lib/api/endpoints/services.ts` to include `buy_x` and `get_y_free` in the `Service`/`DashboardService` type
- [x] 9.2 Update `booking/src/lib/api/endpoints/booking.ts` to send `services: [{service_id, quantity}]` format instead of `service_ids`
- [x] 9.3 Update `booking/src/lib/api/availability.ts` to send quantity data in availability requests (as `quantities` parameter alongside `service_ids`)

## 10. Frontend — Success Confirmation

- [x] 10.1 Update the booking success screen in `BookingForm.tsx` to show the final price paid (including discount if applicable)
- [x] 10.2 Display per-service quantity in the success confirmation (e.g., "Eyebrow Threading ×3")

## 11. Tests

- [x] 11.1 Update existing backend tests (`tests_api.py`, `tests_integrations.py`, `tests_stripe.py`) to use the new `services` format instead of `service_ids`
- [x] 11.2 Add test for `CreateBookingView` with quantities and promotions
- [x] 11.3 Add test for availability endpoints with `quantities` parameter
- [x] 11.4 Add test for `BookingServiceThrough` creation with quantities
- [x] 11.5 Add test for discount calculation with various BOGO configurations
- [x] 11.6 Add test that booking price snapshots remain unchanged when the underlying Event price changes after booking creation
- [x] 11.7 Add test that PRE-PAID bookings discounted to `total_amount=0` skip Stripe and return `payment_required: false`
- [ ] 11.8 Manually test full booking flow with promotion: select service with BOGO → set quantity → see discount in summary → submit → verify Stripe amount and Booking record
- [ ] 11.9 Test booking flow without promotion: select service with no BOGO → verify no discount line → total equals subtotal
- [ ] 11.10 Test mixed booking: multiple services, some with promotions, some without → verify correct aggregated discount
- [ ] 11.11 Test admin: create/edit Event with promotion fields → verify they persist and display correctly
- [ ] 11.12 Test edge cases: quantity=1 with BOGO (no discount), quantity exactly at threshold, quantity above threshold
