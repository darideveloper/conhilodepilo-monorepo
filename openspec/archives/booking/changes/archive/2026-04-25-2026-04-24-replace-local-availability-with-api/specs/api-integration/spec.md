# Spec: Availability API Integration

## ADDED Requirements

### Requirement: Fetch Availability from API
The application MUST query the server for availability based on the current stack of selected services.

#### Scenario: User selects services
1. Given the user has selected one or more services.
2. When the `selectedServices` list updates.
3. Then the system shall call `fetchAvailability` with the list of `serviceId`s.
4. And the `BookingCalendar` shall update its display based on the API response.

#### Scenario: Network Failure
1. Given the API call to fetch availability fails.
2. When the error is returned.
3. Then the `useBookingStore` shall set an error state.
4. And the `BookingCalendar` shall notify the user of the failure.

## REMOVED Requirements

### Requirement: Local Availability Intersection
The application shall no longer compute availability by intersecting service date arrays locally.

#### Scenario: Service selection
1. Given the user has selected one or more services.
2. When the availability check occurs.
3. Then the application shall not execute local intersection logic.

### Requirement: Virtual Availability Injection
The application shall no longer inject virtual limited availability for the next 12 days locally.

#### Scenario: Calendar render
1. Given the calendar renders availability.
2. When the dates are loaded.
3. Then the system shall not inject virtual limited availability dates.
