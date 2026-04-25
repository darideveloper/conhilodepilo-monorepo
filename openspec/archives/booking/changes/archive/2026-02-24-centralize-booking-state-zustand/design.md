# Design: Centralized Booking State Management

## Architectural Reasoning
A central store is necessary to support a multi-step booking flow. Zustand is chosen for its simplicity, small footprint, and excellent React integration.

### Store Structure
The store will be located in `src/store/useBookingStore.ts`. It will handle the primary booking state.

```typescript
interface BookingState {
  // Current selection
  selectedDate: Date | undefined;
  
  // Future-proofing for form data
  formData: {
    fullName: string;
    email: string;
    tourId: string | null;
    guests: number;
    specialRequests: string;
  };

  // Actions
  setSelectedDate: (date: Date | undefined) => void;
  updateFormData: (data: Partial<BookingState['formData']>) => void;
  resetBooking: () => void;
}
```

### Integration Strategy
The `BookingCalendar` will subscribe to `selectedDate` and call `setSelectedDate` on user interaction. This eliminates the need for `useState` inside the component.

## Implementation Details

### src/store/useBookingStore.ts
- Use `create` from `zustand`.
- Initialize `selectedDate` with `undefined` (or current date if preferred).
- Implement atomic actions for state updates.

### src/components/BookingCalendar.tsx
- Remove `useState`.
- Use `useBookingStore` hook to access `selectedDate` and `setSelectedDate`.

## Trade-offs
- **External Dependency**: Introducing Zustand adds a small dependency to the bundle. However, the benefits of cleaner component logic and state persistence outweigh the cost.
- **Client-Side Only**: Zustand state is lost on page refresh unless middleware (like `persist`) is used. For the initial phase, memory-based state is sufficient.
