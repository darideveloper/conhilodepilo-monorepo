# Tasks: Compact Multi-Step Booking Flow

## Step 1: Centralized Navigation System (Zustand)
- [x] Add `currentStep`, `setStep`, `nextStep`, and `prevStep` to `useBookingStore.ts`. <!-- id: 0 -->
- [x] Implement initial validation (e.g., `isDateSelected`) in the store. <!-- id: 1 -->

## Step 2: Calendar Refinement (Step 1)
- [x] Refactor `BookingCalendar.tsx` to include a primary "Next" button. <!-- id: 2 -->
- [x] Bind the "Next" button's disabled state to the store's `selectedDate`. <!-- id: 3 -->
- [x] Add a simple progress indicator (Step 1 of 2). <!-- id: 4 -->

## Step 3: Compact Form Refinement (Step 2)
- [x] Refactor `BookingForm.tsx` to use a responsive grid for field pairs (md+). <!-- id: 5 -->
- [x] Group `fullName`+`email` and `tourId`+`guests` into single rows. <!-- id: 6 -->
- [x] Add a secondary "Back" button to return to the calendar. <!-- id: 7 -->
- [x] Implement general UI compactness improvements (reduced gaps, padding). <!-- id: 8 -->

## Step 4: Layout & Coordination
- [x] Update `src/pages/[id].astro` to manage the multi-step visibility. <!-- id: 9 -->
- [x] Ensure smooth transitions (using simple conditional rendering or `framer-motion` if available). <!-- id: 10 -->
- [x] Verify the complete navigation flow on mobile and desktop. <!-- id: 11 -->

## Step 5: Final Polish
- [x] Review UI for spacing consistency. <!-- id: 12 -->
- [x] Ensure all form fields are accessible and labels are correctly associated. <!-- id: 13 -->
