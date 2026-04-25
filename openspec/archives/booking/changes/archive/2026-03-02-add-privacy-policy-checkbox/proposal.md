# Proposal: Add Required Privacy Policy Checkbox

## Summary
Add a required checkbox to the `BookingForm` that users must check to accept the privacy policy before submitting their booking request. This checkbox will link to the official privacy policy at `https://granadago.com/privacidad/`.

## Motivation
To comply with GDPR and local data protection regulations, users must explicitly consent to the privacy policy before their personal data (Name, Email) is processed and sent to the Stripe payment API.

## Proposed Changes
1.  **Store Update**: Add `privacyAccepted` (boolean) to the `formData` in `useBookingStore`.
2.  **UI Update**: 
    *   Add a Checkbox and Label to the `BookingForm`.
    *   The label will include a link: "He leído y acepto la [política de privacidad](https://granadago.com/privacidad/)".
    *   The checkbox will be `required`.
3.  **Validation**:
    *   Ensure the "Solicitar Reserva" button or the form submission logic validates that the checkbox is checked.

## Impact
- **UI**: New field in the form.
- **State**: New property in Zustand store.
- **Validation**: Prevents submission without consent.
