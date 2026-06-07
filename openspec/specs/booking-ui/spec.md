# booking-ui Specification

## Purpose
TBD - created by archiving change fix-timezone-mismatch. Update Purpose after archive.
## Requirements
### Requirement: Timezone Consistency
The system MUST use `Europe/Madrid` as the primary timezone for business logic and data display.

#### Scenario: Dashboard Timezone Configuration
- GIVEN the dashboard application environment variables
- THEN the `TIME_ZONE` MUST be configured as `Europe/Madrid`.

### Requirement: Accurate Availability Display
The booking calendar MUST display available days exactly as returned by the API, without 1-day shifts due to client-side timezone offsets.

#### Scenario: Parsing Availability Dates
- GIVEN a list of available date strings in "YYYY-MM-DD" format from the API
- WHEN the frontend parses these strings into `Date` objects
- THEN it MUST parse them as local dates (e.g., using `new Date(year, month, day)`) to avoid UTC-to-local shifts.

### Requirement: Persistent Date Integrity
The application MUST maintain the correct selected date after page refreshes, regardless of the user's timezone offset.

#### Scenario: Rehydrating Selected Date
- GIVEN a stored selected date
- WHEN the application rehydrates its state from local storage
- THEN the revived `Date` object MUST represent the same calendar day as originally selected.

### Requirement: Time Slot Selection
The system MUST allow users to select an available time slot after choosing a valid day, and MUST support multiple quantities of the same service via +/- controls in the cart.

#### Scenario: Displaying available times
- **WHEN** a valid day is selected in the booking calendar
- **THEN** the UI MUST present a list of available time slots and require the user to pick one before proceeding to the contact form.

#### Scenario: Service quantity adjustment
- **WHEN** a user increases or decreases the quantity of a selected service via +/- controls
- **THEN** the cart SHALL update the quantity and recalculate the subtotal
- **AND** decreasing from quantity=1 SHALL remove the service entirely

### Requirement: Minimal Contact Information
The system MUST collect only necessary contact information without arbitrary extra fields.

#### Scenario: Completing the contact form
- **WHEN** the user proceeds to the contact info step
- **THEN** they MUST be prompted for Name, Email, and Special Requests, and MUST NOT be prompted for Number of Guests.

### Requirement: Dynamic Privacy Policy Link
The system MUST link to the dynamically configured privacy policy URL in the booking form.

#### Scenario: Accepting privacy policy
- **WHEN** the privacy policy checkbox is displayed
- **THEN** the accompanying text MUST link to the URL provided by the dashboard configuration.

### Requirement: Full Confirmation Summary
The system MUST display a final confirmation summary after a successful booking.

#### Scenario: Showing success screen
- **WHEN** the booking is successfully submitted to the API
- **THEN** the success screen MUST display the collected client Name, Email, Date, Time Slot, and selected Services.

### Requirement: Error Feedback
The system MUST gracefully handle and display API errors during submission.

#### Scenario: Booking submission failure
- **WHEN** the booking submission fails (e.g., slot no longer available)
- **THEN** the UI MUST display a clear error message and allow the user to correct their input without crashing.

### Requirement: Split persistence between Local and Session storage
The application MUST distinguish between persistent user data and ephemeral booking data.

#### Scenario: User Identity Persistence
- **GIVEN** a user has entered their name, email, and phone in the booking form
- **WHEN** the user closes the browser and returns later
- **THEN** the name, email, and phone fields MUST be pre-filled from `localStorage`.

#### Scenario: Booking Session Isolation
- **GIVEN** a user has selected a service, date, and time in one tab
- **WHEN** the user opens the booking form in a NEW tab
- **THEN** the second tab MUST show a fresh booking wizard starting at Step 1, with no service, date, or time selected.

#### Scenario: Exclusive Service Selection via URL
- **GIVEN** a user has an active booking session with "Service A" selected
- **WHEN** the user navigates to the booking app with `?service=B` in the URL (or via `initialServiceId` prop)
- **THEN** the application MUST discard "Service A" and exclusively select "Service B"
- **AND** the user's persistent identity data MUST remain intact.

#### Scenario: Booking Reset Preservation
- **GIVEN** a user has completed a booking or triggered a reset
- **WHEN** the booking state is cleared
- **THEN** the service, date, and time MUST be reset, but the user's name, email, and phone MUST remain in the store.

#### Scenario: Navigation State
- **GIVEN** a user is on Step 3 of the booking form
- **WHEN** the user refreshes the page
- **THEN** the user MUST remain on Step 3.
- **WHEN** the user closes the tab and reopens the form
- **THEN** the user MUST start at Step 1.

### Requirement: Single-Page Application Mode
The booking application MUST operate as a single-page static site where all routing logic for specific services is handled via URL query parameters rather than separate file-system routes.

#### Scenario: Building a single entry point
- **GIVEN** the booking application source code
- **WHEN** the build command is executed
- **THEN** it MUST only generate a single `index.html` file
- **AND** all other service-specific logic MUST be handled by the client-side bundle.

### Requirement: Unified Service Selection
The system MUST use the `service` query parameter as the primary method for auto-selecting a service upon application load.

#### Scenario: Loading with a service parameter
- **GIVEN** a user visits `/?service=123`
- **WHEN** the React application hydrates
- **THEN** it MUST fetch details for service `123` and pre-select it in the booking flow.

### Requirement: Dynamic Page Scaling
The application MUST support dynamic scaling via the `zoom` query parameter to ensure proper rendering when embedded in iframes on the landing page.

#### Scenario: Applying zoom in a static environment
- **GIVEN** the application is served as a static site
- **WHEN** a user visits the application with a `?zoom=X` parameter
- **THEN** the system MUST dynamically apply the zoom percentage to the document body via client-side CSS injection
- **AND** the scaling MUST be applied as early as possible to minimize layout shifts.

### Requirement: Cross-Browser Calendar Compatibility
The booking calendar MUST maintain a consistent and functional grid layout across all supported browsers, specifically ensuring that interactive elements are correctly rendered on macOS Safari without layout collapse or overflow.

#### Scenario: Calendar Layout Stability in Safari
- **WHEN** the user views the booking calendar in Safari on macOS
- **THEN** the month container MUST be rendered as a grid with proper cell alignment to prevent rendering bugs
- **AND** the layout MUST NOT collapse or overflow.

### Requirement: Service Quantity in Cart State
The frontend SHALL track `quantity` per service in the cart state. Adding a service that already exists SHALL increment its quantity instead of being rejected as a duplicate.

#### Scenario: Incrementing quantity for existing service
- **WHEN** a user selects a service that already exists in their cart
- **THEN** the quantity SHALL increment rather than being rejected as a duplicate

#### Scenario: Minimum quantity
- **WHEN** a user tries to reduce the quantity below 1 via the decrement button
- **THEN** the service SHALL be removed from the cart entirely

### Requirement: Price Summary in Booking Form
The booking form (Step 3) SHALL display a price summary showing the original subtotal, any promotional discount, and the final total. Discount SHALL be calculated using the threshold BOGO formula `free_count = min((qty // buy_x) * get_y_free, qty)`.

#### Scenario: Booking with promotion in price summary
- **GIVEN** a cart with "Eyebrow Threading" × 3 at €30 each with Buy 2 Get 1 Free
- **WHEN** the user views the booking summary on Step 3
- **THEN** the UI SHALL display: Subtotal €90, Discount -€30, Total €60

#### Scenario: Booking without promotion
- **GIVEN** a cart with services that have no promotions
- **WHEN** the user views the booking summary
- **THEN** the UI SHALL display only the total (or subtotal equal to total with no discount line)

### Requirement: Promotion Badge on Service Items
The frontend SHALL display a "Buy X Get Y Free" badge on service items that have an active promotion, visible across all booking steps.

#### Scenario: Badge on cart item
- **GIVEN** a service with an active promotion selected in the cart
- **WHEN** the cart is displayed on any booking step
- **THEN** the service item SHALL show a badge with the promotion text (e.g. "Buy 2 Get 1 Free")

#### Scenario: Badge on success confirmation
- **GIVEN** a booking was created with a promotional discount
- **WHEN** the success confirmation screen is displayed
- **THEN** the discount and promotion label SHALL be visible alongside the total

### Requirement: Quantity-Aware Availability Requests
The frontend SHALL send quantity data alongside service IDs when fetching availability, so the backend computes the correct total duration.

#### Scenario: Fetching availability with quantities
- **WHEN** the user has selected Service A × 3 and Service B × 1
- **THEN** the frontend SHALL send both `service_ids=1,2` and `quantities=3,1` to the availability endpoints
- **AND** the backend SHALL return slots with at least `3×durationA + 1×durationB` free time

