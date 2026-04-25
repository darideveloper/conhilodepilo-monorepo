# Tasks: Categorized Service Selection

Implement a new initial screen for categorized service selection, expanding the booking flow to 3 steps.

## Data Refactor

- [x] Create a categorized dummy data structure for `src/data/booking.json`.
- [x] Ensure dummy data includes valid `id`s for services and categories.
- [x] Delete `src/pages/api/tours.ts` as it's no longer needed.
- [x] Update all import statements across the codebase from `../data/tours.json` (and similar paths) to point to `booking.json`.

## State Management & Translations

- [x] Add `serviceTypeId` to `formData` in `src/store/useBookingStore.ts`.
- [x] Update `getInitialAvailability` to handle the nested data structure from `booking.json`.
- [x] Update `updateFormData` to manage `serviceTypeId` and handle service resets if necessary.
- [x] Update `src/lib/i18n/translations.ts` to include keys for a 3-step process (e.g., `step1Of3`, `step2Of3`, `step3Of3`) and remove old `step1Of2`/`step2Of2` if unused.

## UI Implementation: New Screen

- [x] Create `src/components/organisms/BookingServiceSelection.tsx`.
- [x] Implement two dependent `<Select>` components (Service Type -> Service) in the new screen.
- [x] Use API `config` labels (`event_type_label` and `event_label`) for the dropdown labels in the new screen.
- [x] Add a "Continue" button that requires both selections to proceed.
- [x] Ensure the new screen uses the existing `BookingHeader` and layout structure.

## UI Implementation: Existing Screens

- [x] Remove the service selection `<Select>` and related logic from `src/components/organisms/BookingCalendar.tsx`.
- [x] Update `BookingCalendar.tsx` to use the new translation key for "Step 2 of 3".
- [x] Update `src/components/organisms/BookingForm.tsx` to use the new translation key for "Step 3 of 3".
- [x] Update the summary display logic in `BookingForm.tsx` to correctly find the selected service from the nested `booking.json`.

## Flow and Routing

- [x] Update `src/components/organisms/BookingFlow.tsx` to render `BookingServiceSelection` on `currentStep === 1`, `BookingCalendar` on `2`, and `BookingForm` on `3`.
- [x] Update `BookingFlow.tsx` to handle `service_type` (category) from URL parameters.
- [x] Add logic in `BookingFlow` to infer `service_type` if only a `service_id` is provided in the URL and auto-advance to step 2 if a valid service is pre-selected.
- [x] Update `src/pages/[id].astro` to generate paths using the new nested structure.

## Validation

- [ ] Verify that the new 3-step flow works seamlessly (Selection -> Calendar -> Form).
- [ ] Verify that selecting a category filters the service list correctly.
- [ ] Verify that URL parameters for both `service_type` and `service` work as expected (pre-selecting and auto-advancing).
- [ ] Ensure that existing branding (e.g., custom colors, background layout) is correctly applied to the new screen.