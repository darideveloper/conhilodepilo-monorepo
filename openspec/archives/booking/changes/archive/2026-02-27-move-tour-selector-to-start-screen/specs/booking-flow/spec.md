# booking-flow Specification Delta

## ADDED Requirements

### Requirement: Multi-Step Sequence
The booking flow MUST provide a structured, multi-step experience that focuses on one task at a time.

#### Scenario: Step 1 Configuration (NEW)
- **Given** the user is on Step 1 (`currentStep === 1`)
- **Then** the user MUST be able to select a tour from a dropdown.
- **And** the `BookingCalendar` MUST reactively update its availability markers as the tour selection changes.
- **And** the user MUST be able to select a date.

#### Scenario: Step 2 Data Input (MODIFIED)
- **Given** the user is on Step 2 (`currentStep === 2`)
- **Then** the user MUST only be prompted to input personal contact details (`fullName`, `email`, `guests`) and `specialRequests`.
- **And** the `tourId` MUST already be established from the previous step.

#### Scenario: State Initialization (NEW)
- **Given** the user navigates to a tour-specific URL (e.g., `/[tour-id]`)
- **When** the `BookingFlow` component mounts
- **Then** the store's `tourId` MUST be automatically set to the corresponding ID.
- **And** Step 1 MUST display the pre-selected tour and its availability correctly.
