# Proposal: Replace local availability logic with API integration

## Summary
Transition the current reactive, client-side, local-state-based availability system (which uses intersection logic and virtual date injection) to a server-side API-driven model. This will ensure availability data is accurate, real-time, and consistent with the backend.

## Why
The previous client-side logic was prone to inaccuracies and hard to maintain as more services were added. Moving to a server-side API-driven model centralizes source of truth and simplifies the frontend state.

## What Changes
- **Remove:** Client-side availability calculation logic (`getIntersectedAvailability`, `injectVirtualLimitedDates`).
- **Remove:** Redundant `Availability` interface fields if they conflict with API response shapes.
- **Add:** The system SHALL implement an API service layer to fetch availability based on selected services.
- **Update:** `useBookingStore` MUST handle async availability fetching (loading, success, error states).
- **Update:** `BookingCalendar` SHALL handle async state updates.
- **Goal:** The application MUST display accurate availability data from the backend.

## Impact
- Improved data integrity.
- Reduction in client-side code complexity.
- Requires backend endpoint availability.
