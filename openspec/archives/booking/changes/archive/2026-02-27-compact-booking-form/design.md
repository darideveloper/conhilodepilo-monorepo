# Design: Compact Multi-Step Booking Flow

## Architectural Reasoning
The transition to a multi-step flow focuses user attention on one task at a time, which is essential for booking forms where date selection and contact details are two distinct mental processes. Using **Zustand** for centralized state management ensures that navigation logic is scalable and that both `BookingCalendar` and `BookingForm` remain synchronized without complex prop drilling.

## State Management Changes (`useBookingStore.ts`)
The `useBookingStore` will be expanded to support a scalable multi-screen system:
- `currentStep: number` (Default: 1): Represents the current page of the booking journey.
- `setStep: (step: number) => void`: Action to navigate to any step.
- `nextStep: () => void`: Helper to move to the next logical screen.
- `prevStep: () => void`: Helper to return to the previous screen.
- **Validation**:
  - `isDateSelected: boolean` (Derived): Checks if `selectedDate` is defined, used to enable the "Next" button in Step 1.

## Scalable Navigation Components
- **Step 1 (Calendar)**:
  - Add a primary "Continuar con la reserva" button at the bottom of the calendar card.
  - Button state: Disabled if `selectedDate` is undefined; Enabled otherwise.
  - Action: Triggers `nextStep()`.
- **Step 2 (Form)**:
  - Add a secondary "Volver" button at the bottom of the form card.
  - Action: Triggers `prevStep()`.

## Compactness Adjustments
- **Layout Shift**: Instead of the current 50/50 horizontal split on desktop, we will transition to a single centered column that holds the active card. This significantly reduces the horizontal space required and focuses the user.
- **Form Grid**:
  - Row 1: `fullName` (50%) | `email` (50%) on `md` screens and above.
  - Row 2: `tourId` (70%) | `guests` (30%) on `md` screens and above.
  - Row 3: `specialRequests` (100%).
- **Vertical Spacing**: Uniformly reduce `gap-4` to `gap-3` and `gap-2` to `gap-1.5` in all cards.
- **Padding**: Decrease `CardHeader` vertical padding to save space.

## Transition Flow
- **Step 1 -> Step 2**: Valid date selected -> Click "Continuar" -> Card switches to `BookingForm`.
- **Step 2 -> Step 1**: Click "Volver" -> Card switches back to `BookingCalendar`.
- **Data Persistence**: Form data and selected date are held in the store throughout the transitions, ensuring no loss of progress.

## Trade-offs
- **One more click**: Users must click "Next", but the resulting interface is much cleaner and less overwhelming.
- **Mobile First**: This approach is inherently mobile-friendly, as it mirrors the natural mobile flow of one screen at a time.
