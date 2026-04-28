# Design: Timezone Alignment and Date Parsing Correction

## Backend Configuration
The `TIME_ZONE` environment variable in `backend/.env` (and other `.env` files) will be updated from `America/Mexico_City` to `Europe/Madrid`. Since `backend/project/settings.py` already uses `os.getenv("TIME_ZONE", "America/Mexico_City")`, no code changes are required in the backend settings file itself, only configuration updates.

## Frontend Date Handling
The current implementation of `fetchAvailability` in `booking/src/lib/api/availability.ts` uses:
```typescript
available: availableDates.map((d: string) => new Date(d)),
```
In JavaScript, `new Date("YYYY-MM-DD")` is parsed as UTC midnight. For users in timezones west of UTC, this results in the date shifting to the previous day (e.g., "2026-04-26" becomes "2026-04-25 18:00:00" in GMT-6).

### Solution
We will modify the parsing logic to treat these strings as local dates (relative to the user's browser, which aligns with how the Calendar component displays days). The most reliable way to do this without adding extra libraries like `luxon` (since `date-fns` is already present) is to parse the string parts manually or adjust the string format to one that JS parses as local.

**Refined Logic:**
```typescript
available: availableDates.map((d: string) => {
  const [year, month, day] = d.split('-').map(Number);
  return new Date(year, month - 1, day);
}),
This constructor uses local time and prevents any shift.

## Alignment of "Today" Logic
To ensure the frontend "shows the same dashboard timezone", we will remove the redundant `dateObj > today` check in `BookingCalendar.tsx`. 
- **Current problem:** The frontend disables dates based on the user's local browser time, which may conflict with the business's Madrid time (e.g., it's already Monday in Madrid but still Sunday in Mexico).
- **Solution:** Rely exclusively on the `availability.available` array returned by the backend. Since the backend already filters out past dates and times using the correct `Europe/Madrid` context, the frontend should trust this list as the source of truth.

## State Persistence (Zustand Rehydration)
...
In `booking/src/store/useBookingStore.ts`, the `onRehydrateStorage` function revives `selectedDate` and `availability` properties using `new Date(value)`. Since these values are stored as ISO strings (which include time info or are parsed as UTC), we must ensure they are revived correctly to maintain the local date integrity.

We will update the rehydration logic to ensure that `selectedDate` (which is often stored as a full ISO string) is handled consistently with the local calendar display.
