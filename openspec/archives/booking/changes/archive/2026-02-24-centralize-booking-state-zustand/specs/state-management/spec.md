# Spec: Centralized Booking State

This spec defines the requirements for managing booking state centrally.

## ADDED Requirements

### Requirement: Centralized Booking State
The application SHALL manage booking-related data (e.g., selected date, user details) in a centralized store to ensure state consistency across components.

#### Scenario: Update Selected Date
- Given the application is using a centralized booking store.
- When a user selects a date on the `BookingCalendar`.
- Then the `selectedDate` in the centralized store MUST be updated to reflect the choice.

### Requirement: State Reactivity
UI components SHALL automatically react to changes in the centralized booking store.

#### Scenario: Reflect State in UI
- Given the `BookingCalendar` is rendered.
- When the `selectedDate` in the store is changed (either by the calendar or externally).
- Then the calendar's selection and the status display MUST update to show the new date.
