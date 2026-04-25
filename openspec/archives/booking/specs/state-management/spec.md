# Spec: Centralized State Management

## Purpose
This spec defines the requirements for managing application state (such as booking details and user selections) using a centralized store, ensuring data consistency and reactivity across the entire user interface.
## Requirements
### Requirement: Centralized Booking State
The application SHALL manage booking-related data (e.g., selected date, selected services array, user details) in a centralized store to ensure state consistency across components.

#### Scenario: Update Selected Date
- **GIVEN** the application is using a centralized booking store.
- **WHEN** a user selects a date on the `BookingCalendar`.
- **THEN** the `selectedDate` in the centralized store MUST be updated to reflect the choice.

#### Scenario: Add Service to Stack
- **GIVEN** the application is using a centralized booking store.
- **WHEN** a user adds a service to their booking.
- **THEN** the service details MUST be appended to the `selectedServices` array in the store.

### Requirement: State Reactivity
UI components SHALL automatically react to changes in the centralized booking store.

#### Scenario: Reflect State in UI
- **GIVEN** the `BookingCalendar` is rendered.
- **WHEN** the `selectedDate` in the store is changed (either by the calendar or externally).
- **THEN** the calendar's selection and the status display MUST update to show the new date.

### Requirement: Virtual Availability Injection
The state management system SHALL dynamically calculate availability across all selected services and supplement it with a "Virtual Limited" window during initialization.

#### Scenario: Inject Virtual Limited Dates
- **GIVEN** one or more services are selected in the stack.
- **WHEN** availability is loaded from the data source.
- **THEN** the availability MUST be calculated as the intersection of all selected services.
- **AND** the `availability.limited` state MUST be merged with the next 10 days relative to the current time.

### Requirement: API State Integration
The centralized store SHALL encapsulate methods that interact with the **API Service Layer**, ensuring a clean separation between state management and network implementation.

#### Scenario: Dispatch fetchConfig
- **GIVEN** the `useBookingStore` is initialized.
- **WHEN** the `fetchConfig` dispatch action is called.
- **THEN** it MUST invoke the corresponding `api/config` service and update the store's `config` state.

