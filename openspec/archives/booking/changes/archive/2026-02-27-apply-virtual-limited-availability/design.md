# Design: Virtual Limited Availability

## Logic Refactor
The injection of virtual limited dates will happen in the `useBookingStore.ts` to centralize the availability logic.

### 1. Store Update (`src/store/useBookingStore.ts`)
We will add a helper function `injectVirtualLimitedDates` that takes existing `limited` and `booked` dates and returns a new `limited` array including the next 10 days.

```typescript
const injectVirtualLimitedDates = (limited: Date[], booked: Date[]): Date[] => {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  
  const virtualLimited: Date[] = [...limited];
  const bookedStrings = new Set(booked.map(d => d.toDateString()));
  const limitedStrings = new Set(limited.map(d => d.toDateString()));

  for (let i = 1; i <= 10; i++) {
    const d = new Date(today);
    d.setDate(today.getDate() + i);
    const dateStr = d.toDateString();
    
    if (!bookedStrings.has(dateStr) && !limitedStrings.has(dateStr)) {
      virtualLimited.push(d);
    }
  }
  
  return virtualLimited;
};
```

This helper will be called inside `getInitialAvailability`.

### 2. Component Synchronization
Since `BookingCalendar.tsx` uses the `availability` object from the store, it will automatically render these dates with the `isLimited` modifier and show the "Limitada" status in `StatusDetails`.

## Verification Plan
1.  **Selection**: Select any tour.
2.  **Visual Check**: Verify that the next 10 days from today (excluding past/today) are highlighted in Amber/Gold.
3.  **Override Check**: If a date within those 10 days is explicitly "Booked" in the JSON, it must remain "Booked" (Slate/Gray).
4.  **Status Check**: Click on one of these "Virtual Limited" dates and verify the `StatusDetails` card shows "Limitada".
