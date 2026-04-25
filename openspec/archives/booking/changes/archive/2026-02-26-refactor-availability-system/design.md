# Design: Refactor Availability System

## Overview
The availability system will be refactored to be tour-centric. Each tour in the JSON database will define its recurring available days of the week. The application will then generate concrete dates for the calendar based on these rules.

## Data Structure Changes
Each object in `src/data/tours.json` will be updated to include a `dates` object:
```json
{
  "id": "alhambra-completa",
  ...
  "dates": {
    "available": ["2026-03-01", "2026-03-02"],
    "limited": ["2026-03-03"],
    "booked": ["2026-03-04"]
  }
}
```

## State Logic
The `useBookingStore` will be enhanced to:
1.  Store the full `tours` data.
2.  Provide the `available`, `limited`, and `booked` dates for the selected `tourId`.
3.  When `updateFormData({ tourId: '...' })` is called, the store will automatically update the calendar's availability data.

## Component Refactoring
### `BookingCalendar.tsx`
- Remove `bookingData` mock.
- Use `useBookingStore` to get `availableDates`, `limitedDates`, and `bookedDates`.
- Update the calendar modifiers and disabled days based on this data.

### `BookingForm.tsx`
- No major changes needed other than ensuring `tourId` updates correctly in the store, which it already does.

## Future Considerations
- Adding specific `blockedDates` for holidays or guide absences.
- Integrating with an external booking engine or API for real-time availability.
