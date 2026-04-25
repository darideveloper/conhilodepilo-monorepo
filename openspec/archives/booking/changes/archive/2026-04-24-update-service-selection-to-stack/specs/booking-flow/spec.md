## MODIFIED Requirements
### Requirement: Multi-Step Sequence
The booking flow MUST provide a structured, multi-step experience that focuses on one task at a time.

#### Scenario: Step 1 Service Selection (MODIFIED)
- **Given** the user is on Step 1 (`currentStep === 1`)
- **When** the `BookingServiceSelection` screen renders
- **Then** the user MUST be able to select a "Service Type" (category) and "Service" (tour) and add them to their stack.
- **And** the user MUST NOT be able to proceed to Step 2 until at least one service is in the stack.

#### Scenario: State Initialization (MODIFIED)
- **Given** the user navigates to a service-specific URL (e.g., `/[service-id]`) or provides URL parameters.
- **When** the `BookingFlow` component mounts.
- **THEN** the system MUST perform an **idempotent** addition: it SHALL only add the service to the `selectedServices` stack if it is not already present.
- **AND** the application SHOULD advance to Step 2 (`BookingCalendar`) automatically if Step 1 is fulfilled by this initialization.
