# Design: Default-Available Refactor

## Architectural Change
We are moving from an **Inclusive** availability model (listing everything available) to an **Exclusive** model (listing only exceptions to the default "available" state).

### 1. Data Layer (`src/data/tours.json`)
The `dates` object for each tour will now only contain exceptions. The `available` property will be removed.

```json
"dates": {
    "limited": ["2026-03-01", "2026-03-07"],
    "booked": []
}
```

### 2. State Layer (`src/store/useBookingStore.ts`)
Update the `Availability` interface and the parsing logic.

```typescript
// src/store/useBookingStore.ts

interface Availability {
  limited: Date[];
  booked: Date[];
  // available is removed
}

const getInitialAvailability = (tourId: string | null): Availability => {
  const tour = toursData.find(t => t.id === tourId);
  if (!tour || !tour.dates) {
    return { limited: [], booked: [] };
  }
  
  const parseDate = (dateStr: string) => {
    const [year, month, day] = dateStr.split('-').map(Number);
    return new Date(year, month - 1, day);
  };

  return {
    limited: (tour.dates.limited || []).map(parseDate),
    booked: (tour.dates.booked || []).map(parseDate),
  };
};
```

### 3. UI Logic Layer (`src/components/organisms/BookingCalendar.tsx`)
The `modifiers` and `getStatus` logic will be updated to treat all future dates as "available" by default.

```typescript
// src/components/organisms/BookingCalendar.tsx

const modifiers = useMemo(() => ({
  isBooked: (d: Date) => d > today && availability.booked.some((date: Date) => date.toDateString() === d.toDateString()),
  isLimited: (d: Date) => d > today && availability.limited.some((date: Date) => date.toDateString() === d.toDateString()),
  isAvailable: (d: Date) => d > today && 
    !availability.booked.some((date: Date) => date.toDateString() === d.toDateString()) &&
    !availability.limited.some((date: Date) => date.toDateString() === d.toDateString()),
}), [availability, today]);

const getStatus = (d: Date | undefined): StatusKey => {
  if (!d || d <= today) return 'standard';
  const dateStr = d.toDateString();
  if (availability.booked.some((date: Date) => date.toDateString() === dateStr)) return 'booked';
  if (availability.limited.some((date: Date) => date.toDateString() === dateStr)) return 'limited';
  return 'available';
};
```
