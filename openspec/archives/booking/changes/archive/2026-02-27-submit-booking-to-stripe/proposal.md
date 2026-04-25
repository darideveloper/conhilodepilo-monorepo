# Submit Booking to Stripe

Submit the booking form data to the Stripe-backed services endpoint and show a loading state during the process.

## Summary
- **What**: Integrate the booking form with a Stripe-backed payment API.
- **Why**: Enable users to finalize their booking by paying for it through a secure service.
- **Key Features**:
  - Asynchronous form submission with loading feedback.
  - Integration with an external API using environment variables for configuration.
  - Comprehensive payload construction from global store state.

## Affected Areas
- **`src/components/organisms/BookingForm.tsx`**: Add submission logic and UI feedback.
- **`.env.example`**: New required environment variables.
- **`src/store/useBookingStore.ts`**: Potential store updates (if needed).

For more technical details, refer to [Design Specification](./specs/booking-submission/design.md).
