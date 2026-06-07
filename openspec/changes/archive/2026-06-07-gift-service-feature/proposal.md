## Why

Clients frequently want to book services as gifts for friends and family. Currently the system has no way to distinguish between a buyer and a service recipient — all bookings assume the person filling the form is the one receiving the service. This forces gift buyers to book in their own name and then manually coordinate with the recipient, creating confusion in the dashboard and no clear communication to either party.

## What Changes

- Add a "¿Es un servicio de regalo?" checkbox to the booking form (step 3)
- When checked, show recipient name + email fields conditionally
- Store gift metadata on the Booking model: `is_gift`, `buyer_name`, `buyer_email`, `recipient_name`, `recipient_email`
- `client_name` / `client_email` on Booking will always represent the **final service recipient** (buyer if not gift, gift target if gift)
- Dashboard admin displays buyer and recipient clearly, with a visual gift badge
- Send **two emails** when a booking is a gift:
  - To the **buyer**: confirmation of purchase with recipient details
  - To the **recipient**: notification that they received a gift, with buyer info
- Stripe webhook sends both emails on payment completion for pre-paid gifts
- Existing bookings are backward-compatible: `is_gift=False`, `buyer_name=buyer_email=client_name/client_email` after migration

## Capabilities

### New Capabilities
- `gift-service`: Complete gift flow — form UI toggle, conditional recipient fields, dual-email notification, admin display

### Modified Capabilities
- `dashboard-models`: Booking model gains `is_gift`, `buyer_name`, `buyer_email`, `recipient_name`, `recipient_email` fields
- `api-contracts`: POST `/api/bookings/` payload and response include gift fields; validation requires recipient name+email when `isGift=true`
- `confirmation-email`: Email system sends two distinct emails on gift bookings (buyer confirmation + recipient notification), each with role-specific copy
- `booking-ui`: Booking form step 3 adds gift checkbox with conditional recipient fields; submit payload includes gift data

## Impact

- **Dashboard/API**: Booking model migration, CreateBookingView payload parsing, admin display, email sending logic
- **Frontend (booking)**: Zustand store schema, BookingForm component, API client types, i18n translations
- **Email**: New template variants or conditional blocks, dual-send logic
- **Stripe webhook**: Must trigger both emails on `PAID` status change for gift bookings
- **No impact on**: Availability logic, pricing engine, Google Calendar sync (beyond description text), landing page
