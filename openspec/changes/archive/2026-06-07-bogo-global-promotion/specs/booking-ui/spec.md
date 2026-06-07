## MODIFIED Requirements

### Requirement: Price Summary in Booking Form
The booking form (Step 3) SHALL display a price summary showing the original subtotal, any promotional discount, and the final total. Discount SHALL be calculated using the threshold BOGO formula `free_count = min((qty // buy_x) * get_y_free, qty)`. The `buy_x` and `get_y_free` values SHALL be read from the global config (`AppConfig`), not from per-service data.

#### Scenario: Booking with promotion in price summary
- **GIVEN** a cart with "Eyebrow Threading" × 3 at €30 each and the global promotion is Buy 2 Get 1 Free
- **WHEN** the user views the booking summary on Step 3
- **THEN** the UI SHALL display: Subtotal €90, Discount -€30, Total €60

#### Scenario: Booking without promotion
- **GIVEN** a cart with services that have no global promotion configured
- **WHEN** the user views the booking summary
- **THEN** the UI SHALL display only the total (or subtotal equal to total with no discount line)

#### Scenario: Exact threshold discount applied correctly
- **GIVEN** a cart with "Eyebrow Threading" × 2 at €30 each and the global promotion is Buy 2 Get 1 Free
- **WHEN** the price summary is calculated
- **THEN** the discount SHALL be -€30 (1 free item)
- **AND** the guard condition SHALL use `qty >= buy_x`, not `qty > buy_x`

### Requirement: Promotion Badge on Service Items
The frontend SHALL display a "Buy X Get Y Free" badge on service items when the global promotion is active, visible across all booking steps. The badge text SHALL be derived from the global config values, not per-service data.

#### Scenario: Badge on cart item
- **GIVEN** the global promotion is active (e.g. buy_x=2, get_y_free=1)
- **WHEN** any service is displayed in the cart on any booking step
- **THEN** the service item SHALL show a badge with the promotion text (e.g. "Buy 2 Get 1 Free")

#### Scenario: Badge on success confirmation
- **GIVEN** a booking was created with a promotional discount
- **WHEN** the success confirmation screen is displayed
- **THEN** the discount and promotion label SHALL be visible alongside the total

#### Scenario: No badge when promotion disabled
- **GIVEN** the global promotion is disabled (buy_x=0, get_y_free=0)
- **WHEN** any service is displayed in the cart
- **THEN** no promotion badge SHALL be shown

## ADDED Requirements

### Requirement: Frontend Reads Promotion from Global Config
The frontend SHALL read `buy_x` and `get_y_free` from the `AppConfig` object (fetched from `/api/config/`), not from the individual service API data. The `DashboardService` type SHALL NOT include promotion fields.

#### Scenario: Promotion values come from config
- **GIVEN** the frontend has loaded the AppConfig with `buy_x=2` and `get_y_free=1`
- **WHEN** `getServicePromotion()` is called for any service
- **THEN** it SHALL return the global values from AppConfig
- **AND** it SHALL NOT depend on any service-specific fields
