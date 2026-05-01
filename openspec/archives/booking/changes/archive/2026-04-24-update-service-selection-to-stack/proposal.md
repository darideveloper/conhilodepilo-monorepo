# Change: Implement Multi-Service Selection (Stack Builder)

## Why
Currently, the application strictly limits users to booking a single service at a time. To improve the user experience and potentially increase revenue, users should be able to select, stack, and book multiple services in a single checkout flow.

## What Changes
- Transition the state store to handle an array of `selectedServices` rather than a single `serviceId`.
- Update the UI in Step 1 to act as a "builder," allowing users to add multiple services to a visual stack before proceeding.
- Update the availability logic to calculate the intersection of available dates for all selected services.
- Display a summary of all selected services in the final checkout form.
- Update the API payload to submit `serviceIds` instead of a single `serviceId`.
- **BREAKING**: The dashboard endpoint must be modified to accept and process an array of `serviceIds`.

## Impact
- Affected specs: `booking-flow`, `state-management`, `booking-form`, `booking-submission`
- Affected code:
  - `src/store/useBookingStore.ts`
  - `src/components/organisms/BookingServiceSelection.tsx`
  - `src/components/organisms/BookingCalendar.tsx`
  - `src/components/organisms/BookingForm.tsx`
  - `src/lib/api/endpoints/booking.ts`
