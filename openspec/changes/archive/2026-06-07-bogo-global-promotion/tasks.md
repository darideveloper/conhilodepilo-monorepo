## 1. Data Model & Migration

- [x] 1.1 Add `buy_x` (PositiveIntegerField, default=0) and `get_y_free` (PositiveIntegerField, default=0) fields to `CompanyProfile` model with help text
- [x] 1.2 Remove `buy_x` and `get_y_free` fields from `Event` model
- [x] 1.3 Generate migration `0017` — this MUST: (a) AddField buy_x/get_y_free to CompanyProfile, (b) RemoveField buy_x/get_y_free from Event
- [x] 1.4 Apply migration to dev database and verify tables have correct columns

## 2. Pricing Utility — Pure Function Refactor

- [x] 2.1 Refactor `calculate_service_discount()` to pure function: `(unit_price, quantity, buy_x, get_y_free)` — no ORM/Event dependency
- [x] 2.2 Refactor `calculate_booking_totals()` to accept optional `(buy_x, get_y_free)` params with fallback to `CompanyProfile.get_solo()`
- [x] 2.3 Update `tests_pricing.py`: refactor tests to call pure function with explicit params instead of creating Event objects

## 3. Views & Serializers

- [x] 3.1 In `CreateBookingView.post()`: read `buy_x`/`get_y_free` from `CompanyProfile.get_solo()` and pass to `calculate_booking_totals()`
- [x] 3.2 Remove `buy_x`/`get_y_free` fields from `EventSerializer` in `serializers.py`
- [x] 3.3 Add `buy_x`/`get_y_free` fields to `CompanyProfileSerializer` fields list

## 4. Admin UI

- [x] 4.1 Remove `buy_x`/`get_y_free` from `EventAdmin.fieldsets` in `admin.py`
- [x] 4.2 Add `buy_x`/`get_y_free` to `CompanyProfileAdmin` fieldsets (add a new "Promotions" tab or section)

## 5. Email Notification — Quantity & Price Display

- [x] 5.1 Update `send_confirmation_email()` in `utils/email.py`: change `booking.services.all()` to `booking.booking_services.select_related('event').all()`
- [x] 5.2 Build service list entries with `quantity`, `unit_price`, and `subtotal` from through model data
- [x] 5.3 Add `original_amount`, `discount_amount`, and `total_amount` to email template context
- [x] 5.4 Update plain text email body to show quantity and price per service, plus discount summary
- [x] 5.5 Update HTML template `booking_confirmation.html`: add "Cant." column, show subtotal per line, add price summary section (subtotal, discount, total)
- [x] 5.6 Update `tests_email.py` to expect quantity and price data in service list

## 6. Frontend — Types & Config

- [x] 6.1 Add `buy_x: number` and `get_y_free: number` to `AppConfig` interface in `useBookingStore.ts`
- [x] 6.2 Remove `buy_x` and `get_y_free` from `DashboardService` type in `services.ts`

## 7. Frontend — Promotion Logic Refactor

- [x] 7.1 Refactor `getServicePromotion()` in `BookingServiceSelection.tsx` to read from `config` (global AppConfig) instead of per-service data
- [x] 7.2 Refactor `priceSummary` in `BookingForm.tsx` to read `buy_x`/`get_y_free` from `config` instead of from service object
- [x] 7.3 **Bug fix**: Change discount condition from `qty > buy_x` to `qty >= buy_x` in `BookingForm.tsx:46`

## 8. Frontend — Promotion Badge on All Steps

- [x] 8.1 Ensure promotion badge ("Buy X Get Y Free") renders on Step 3 (booking form) next to each service name in the selected services list
- [x] 8.2 Ensure promotion badge and discount info renders on the success confirmation screen after booking submission

## 9. Tests

- [x] 9.1 Update `tests_bogo.py`: test data no longer sets buy_x/get_y_free on Event; set them on CompanyProfile instead; update API tests to expect promotion fields in config endpoint, not services endpoint
- [x] 9.2 Run existing backend test suite and fix any failures caused by the model/serializer changes
- [ ] 9.3 Manual test: create a booking with global promotion active → verify email shows quantities, prices, and discount
- [ ] 9.4 Manual test: create a booking without promotion → verify email shows total only, no discount line
- [ ] 9.5 Manual test: verify frontend badge shows on all steps when promotion active
- [ ] 9.6 Manual test: verify exact-threshold quantity (e.g. qty=2 with Buy 2 Get 1 Free) shows correct discount in frontend preview
