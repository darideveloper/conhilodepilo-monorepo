## 1. Database Migration

- [x] 1.1 Add `is_gift`, `buyer_name`, `buyer_email`, `recipient_name`, `recipient_email` fields to `Booking` model in `dashboard/booking/models.py`
- [x] 1.2 Run `python manage.py makemigrations` to generate the schema migration
- [x] 1.3 Create a data migration (`python manage.py makemigrations booking --empty`) that sets `is_gift=False`, `buyer_name=client_name`, `buyer_email=client_email` for all existing records where these fields are null
- [x] 1.4 Run migrations and verify schema in test database

## 2. Backend API — Create Booking Endpoint

- [x] 2.1 Update `CreateBookingView.post()` in `dashboard/booking/views.py` to parse `isGift`, `buyerName`, `buyerEmail` from request payload
- [x] 2.2 Add validation: if `isGift=True`, require `buyerName` and `buyerEmail`; return 400 if missing
- [x] 2.3 Map payload fields to model: when `isGift=True`, store `client_name/client_email` from recipient fields, `buyer_name/buyer_email` from buyer fields; when `isGift=False`, set `buyer_name/buyer_email` from `client_name/client_email`
- [x] 2.4 Update booking creation in the atomic transaction block to include new gift fields
- [x] 2.5 Add `is_gift`, `buyer_name`, `buyer_email` to the API response payload
- [x] 2.6 Update the Stripe webhook handler to trigger both emails when `booking.is_gift=True`

## 3. Email System — Dual Gift Emails

- [x] 3.1 Create `send_gift_confirmation_emails(booking)` in `dashboard/utils/email.py` that sends two role-specific emails (buyer + recipient)
- [x] 3.2 Extract shared email rendering into a reusable `_build_base_context` + `_send_email` + `_build_plain_text` helpers used by both the existing and gift email functions
- [x] 3.3 Update the email template `dashboard/project/templates/email/booking_confirmation.html` to accept `email_role` parameter and render conditional gift/buyer/recipient greeting and body copy
- [x] 3.4 Add buyer-specific copy: "Has regalado una cita a [recipient_name]" in subject and greeting
- [x] 3.5 Add recipient-specific copy: "Has recibido un regalo de [buyer_name]" in subject and greeting
- [x] 3.6 Wire the new `send_gift_confirmation_emails` into `CreateBookingView` (for CONFIRMED status) and `StripeWebhookView` (for PAID status)
- [x] 3.7 Ensure each email is sent in its own try/except so failure of one does not block the other

## 4. Frontend — Zustand Store

- [x] 4.1 Add `isGift`, `giftTargetName`, `giftTargetEmail` fields to `formData` interface in `booking/src/store/useBookingStore.ts`
- [x] 4.2 Update `hybridStorage.setItem` to persist `giftTargetName` and `giftTargetEmail` in sessionStorage
- [x] 4.3 Update `resetBooking` to clear the three new gift fields
- [x] 4.4 Update `partialize` to include new fields in the persisted state

## 5. Frontend — Booking Form (Step 3)

- [x] 5.1 Add gift checkbox "¿Es un servicio de regalo?" to `BookingForm.tsx` after the phone field, styled consistently with the privacy checkbox
- [x] 5.2 Add conditional recipient name + email fields that appear when checkbox is checked, with required validation
- [x] 5.3 Add clear/transition behavior: unchecking the checkbox hides fields and clears entered values
- [x] 5.4 Update `handleSubmit` to map fields correctly for API payload: when `isGift=True`, send `clientName`/`clientEmail` from recipient fields and `buyerName`/`buyerEmail` from the form's name/email fields
- [x] 5.5 Update the success confirmation section to display the recipient name when `isGift=True`

## 6. Frontend — API Client & Types

- [x] 6.1 Update `BookingPayload` interface in `booking/src/lib/api/endpoints/booking.ts` with optional `isGift`, `buyerName`, `buyerEmail` fields

## 7. Frontend — Translations

- [x] 7.1 Add gift-related translation keys to `booking/src/lib/i18n/translations.ts`:
  - `form.isGift`: "¿Es un servicio de regalo?" / "Is this a gift service?"
  - `form.giftTargetName`: "Nombre del destinatario" / "Recipient name"
  - `form.giftTargetEmail`: "Email del destinatario" / "Recipient email"

## 8. Dashboard Admin

- [x] 8.1 Add `is_gift`, `buyer_name`, `buyer_email` to `BookingAdmin.fieldsets` under "Client Information"
- [x] 8.2 Add read-only status for gift fields
- [x] 8.3 Add a gift badge (e.g., "🎁 Regalo") to `get_client_name` or as a new list display column
- [x] 8.4 Add `is_gift`, `buyer_name`, `buyer_email`, `recipient_name`, `recipient_email` to search fields if appropriate

## 9. Google Calendar Sync

- [x] 9.1 Update event description construction in `dashboard/utils/google_calendar.py` to include `buyer_name` in the description when `booking.is_gift=True`

## 10. Landing Page — Success Page

- [x] 10.1 Update `landing/src/pages/success.astro` copy to clarify that for gift bookings, details were sent to both the buyer and the recipient

## 11. Tests

- [x] 11.1 Write `GiftEmailTest` in `tests_email.py`: verify two emails sent with correct role-specific content for gift bookings
- [x] 11.2 Write `GiftBookingApiTest` (in `tests_api.py` or similar): POST `/api/bookings/` with `isGift=true` and verify correct model fields
- [x] 11.3 Write `GiftBookingValidationTest`: POST with `isGift=true` but missing recipient fields returns 400
- [x] 11.4 Write `GiftBookingBackwardCompatTest`: POST without gift fields creates booking with correct defaults
- [x] 11.5 Write `GiftStripeWebhookTest` in `tests_stripe.py`: verify dual email sent on webhook for gift bookings
- [x] 11.6 Write `GiftModelMigrationTest` in `tests.py` or `tests_models.py`: verify existing bookings get correct default values after migration
- [x] 11.7 Verify all existing tests still pass after changes
