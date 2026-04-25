# Tasks: Move Tour Selector to Start Screen

## Step 1: Initialization Logic
- [x] Move the `initialTourId` handling from `BookingForm.tsx` to `BookingFlow.tsx` or `BookingCalendar.tsx`. <!-- id: 0 -->
- [x] Ensure the store is updated with the URL tour selection on component mount. <!-- id: 1 -->

## Step 2: Calendar Screen (Step 1)
- [x] Add the `Tour` selection dropdown to `BookingCalendar.tsx` (above the legend). <!-- id: 2 -->
- [x] Connect the `Select` component to `updateFormData({ tourId: e.target.value })`. <!-- id: 3 -->
- [x] Adjust vertical spacing to keep the card compact. <!-- id: 4 -->

## Step 3: Form Screen (Step 2)
- [x] Remove the `Tour` selection field from `BookingForm.tsx`. <!-- id: 5 -->
- [x] Refine the grid layout for the remaining fields (`fullName`, `email`, `guests`). <!-- id: 6 -->
- [x] Ensure vertical padding remains consistent across screens. <!-- id: 7 -->

## Step 4: Verification & Validation
- [x] Verify that switching the tour in Step 1 immediately updates the calendar markers. <!-- id: 8 -->
- [x] Verify that the form correctly persists and displays only personal details in Step 2. <!-- id: 9 -->
- [x] Check accessibility (labels, ARIA) for the new tour selection placement. <!-- id: 10 -->
