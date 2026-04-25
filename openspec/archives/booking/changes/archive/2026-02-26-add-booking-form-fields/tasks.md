# Tasks: Add Booking Form Fields

- [x] **Research & Setup**
    - [x] Verify `src/data/tours.json` structure for Tour Select population.
    - [x] Confirm layout constraints in `src/pages/index.astro`.

- [x] **UI Atoms Development**
    - [x] Create `src/components/atoms/ui/label.tsx`.
    - [x] Create `src/components/atoms/ui/input.tsx`.
    - [x] Create `src/components/atoms/ui/textarea.tsx`.
    - [x] Create `src/components/atoms/ui/select.tsx` (using styled native select for simplicity).

- [x] **Form Component Implementation**
    - [x] Create `src/components/organisms/BookingForm.tsx`.
    - [x] Implement fields: Full Name, Email, Tour, Guests, Special Requests.
    - [x] Connect fields to `useBookingStore`.

- [x] **Layout Integration**
    - [x] Create `src/components/organisms/BookingWidget.tsx` to combine `BookingForm` and `BookingCalendar`.
    - [x] Update `src/pages/index.astro` to use `BookingWidget` instead of `BookingCalendar`.
    - [x] Ensure responsive behavior (Form on top of Calendar on mobile, Left of Calendar on Desktop).

- [x] **Validation & Refinement**
    - [x] Apply brand colors to all new components.
    - [x] Verify store updates on input change.
    - [x] Test layout on different screen sizes.
