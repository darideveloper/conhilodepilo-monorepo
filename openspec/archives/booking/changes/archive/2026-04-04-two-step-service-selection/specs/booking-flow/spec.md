# Spec Delta: Three-Step Booking Flow

## MODIFIED Requirements

### Requirement: Multi-Step Sequence
The booking flow MUST provide a structured, multi-step experience that focuses on one task at a time.

#### Scenario: Step 1 Service Selection (MODIFIED)
- **Given** the user is on Step 1 (`currentStep === 1`)
- **When** the `BookingServiceSelection` screen renders
- **Then** the user MUST be able to select a "Service Type" (category) from a dropdown.
- **And** the user MUST then be able to select a "Service" (tour) from a second, dependent dropdown.
- **And** the "Service" selection MUST filter based on the chosen "Service Type".
- **And** selecting a new "Service Type" MUST clear the "Service" selection if it's no longer valid.
- **And** the user MUST NOT be able to proceed to Step 2 until both are selected.

#### Scenario: Step 2 Date Selection (MODIFIED)
- **Given** the user has progressed to Step 2 (`currentStep === 2`)
- **When** the `BookingCalendar` screen renders
- **Then** the user MUST only be presented with the calendar to select a date.
- **And** the user MUST NOT see the service selection dropdowns on this screen.
- **And** the `BookingCalendar` MUST reactively display availability markers based on the service selected in Step 1.

#### Scenario: Step 3 Data Input (MODIFIED)
- **Given** the user has progressed to Step 3 (`currentStep === 3`)
- **When** the `BookingForm` screen renders
- **Then** the user MUST only be prompted to input personal contact details (`fullName`, `email`, `guests`) and `specialRequests`.

#### Scenario: State Initialization (MODIFIED)
- **Given** the user navigates to a service-specific URL (e.g., `/[service-id]`) or provides URL parameters
- **When** the `BookingFlow` component mounts
- **Then** the store's `serviceId` MUST be automatically set to the corresponding ID.
- **And** the `serviceTypeId` MUST be automatically inferred and set based on the `serviceId`.
- **And** the application SHOULD advance to Step 2 (`BookingCalendar`) automatically since Step 1 is fulfilled.