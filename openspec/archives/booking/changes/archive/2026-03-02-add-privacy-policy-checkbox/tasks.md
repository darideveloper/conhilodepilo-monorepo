# Tasks: Add Required Privacy Policy Checkbox

## Setup
- [x] Initialize change: `2026-03-02-add-privacy-policy-checkbox`

## State Management
- [x] Add `privacyAccepted` to `BookingState['formData']` interface in `src/store/useBookingStore.ts`.
- [x] Update initial `formData` state to include `privacyAccepted: false` in `src/store/useBookingStore.ts`.
- [x] Update `resetBooking` to reset `privacyAccepted` to `false`.

## UI Implementation
- [x] Modify `src/components/organisms/BookingForm.tsx`:
    - [x] Update `handleChange` to handle checkbox input (if needed) or add a separate `handleCheckboxChange`.
    - [x] Add checkbox and label with a link to `https://granadago.com/privacidad/` above the form buttons.
    - [x] Style checkbox with Tailwind to match brand color (e.g., `text-brand-red`).
    - [x] Add `required` attribute to the checkbox input.

## Validation
- [x] Update `handleSubmit` in `src/components/organisms/BookingForm.tsx` to explicitly check `formData.privacyAccepted`.

## Verification
- [x] Verify that the form cannot be submitted without checking the privacy policy.
- [x] Verify that clicking the link "política de privacidad" opens `https://granadago.com/privacidad/` in a new tab.
- [x] Verify that the state is reset when `resetBooking` is called.
