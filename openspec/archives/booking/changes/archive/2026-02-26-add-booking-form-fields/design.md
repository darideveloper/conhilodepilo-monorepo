# Design: Booking Form Integration

## Architecture
The booking system will follow the Atomic Design pattern already established in the project.

### Component Hierarchy
- **Atoms (UI):**
    - `Input`: Standard text input.
    - `Label`: Accessible label for inputs.
    - `Textarea`: Multi-line text input for special requests.
    - `Select`: Dropdown for tour selection.
- **Organisms:**
    - `BookingForm`: Manages the state and layout of the input fields.
    - `BookingWidget`: A new parent organism that wraps `BookingForm` and `BookingCalendar` to manage the responsive layout (flex-row on desktop, flex-col on mobile).

## State Management
We will continue using `useBookingStore` from `src/store/useBookingStore.ts`.
- Form fields will use the `updateFormData` action on `onChange` or `onBlur`.
- The `tourId` select will be populated using data from `src/data/tours.json`.

## Styling & Branding
- **Colors:**
    - Primary actions and focus rings: `brand-red` (`--color-brand-red`).
    - Text and borders: `brand-charcoal` (`--color-brand-charcoal`).
    - Backgrounds: `background` / `brand-cream`.
- **Layout:**
    - On `lg` screens, the widget will have a max-width and use a two-column layout.
    - The `BookingCalendar` will remain on the right, and the `BookingForm` will be on the left.

## Data Flow
1. User enters data in `BookingForm`.
2. `BookingForm` calls `updateFormData` in Zustand store.
3. User selects a date in `BookingCalendar`.
4. `BookingCalendar` calls `setSelectedDate` in Zustand store.
5. All data is ready in the store for submission (submission logic not part of this specific task but prepared by it).
