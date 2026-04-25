# Spec Delta: Availability System

## MODIFIED Requirements

### Requirement: tours-data-model
Each tour in the data source MUST include explicit scheduling information.

- **ADDED** Each tour entry in `src/data/tours.json` MUST contain a `dates` object.
- **ADDED** The `dates` object MUST include `available`, `limited`, and `booked` keys, each being an array of date strings (e.g., "2026-03-25").

#### Scenario: Define tour availability
- **Given** I am editing `src/data/tours.json`
- **When** I add `"dates": { "available": ["2026-03-25"], "limited": [], "booked": [] }` to a tour
- **Then** that tour should be considered available only on March 25th, 2026.

### Requirement: availability-state-sync
The system MUST synchronize the calendar's availability with the selected tour.

- **MODIFIED** The `useBookingStore` MUST provide the availability data for the selected tour.
- **ADDED** When the `tourId` in `formData` changes, the `calendarAvailability` MUST be updated in the store.

#### Scenario: Change tour updates calendar
- **Given** The user has selected "Alhambra Completa"
- **And** the calendar shows its specific availability
- **When** the user changes the selected tour to "Sacromonte"
- **Then** the calendar MUST immediately update to show "Sacromonte"'s specific available, limited, and booked dates.

### Requirement: dynamic-calendar-display
The calendar MUST display availability based on the store's data.

- **REMOVED** Hardcoded mock dates for `available`, `booked`, and `limited`.
- **MODIFIED** The `BookingCalendar` MUST use the `dates` provided by `useBookingStore`.
- **ADDED** Days marked as `booked` MUST be disabled in the calendar.

#### Scenario: Display tour-specific availability
- **Given** A tour with `availableDays: [2, 4]` (Tue, Thu) is selected
- **When** the `BookingCalendar` renders
- **Then** only Tuesdays and Thursdays should have the "available" visual modifier.
- **And** other days should be disabled or have the "standard" style.
