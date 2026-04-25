# booking-form Specification Delta

## MODIFIED Requirements

### Requirement: Responsive Layout
The booking interface MUST adapt its layout based on the screen size and the current step.

#### Scenario: Multi-Step Sequence (NEW)
- **Given** the user is on Step 1 (`currentStep === 1`)
- **Then** the `BookingCalendar` MUST be primary and visible.
- **When** the user selects a date and clicks "Next"
- **Then** the `BookingForm` MUST be displayed (Step 2).

#### Scenario: Compact Field Grouping (NEW)
- **Given** the user is on Step 2 (Form) and screen width is 768px (md) or greater
- **Then** `Nombre Completo` and `Email` MUST be displayed in the same row.
- **And** `Tour` and `Número de personas` MUST be displayed in the same row.
- **And** `Peticiones especiales` MUST span the full width of the form.

## NEW Requirements

### Requirement: State Synchronization & Navigation
The booking flow MUST persist state across steps and provide clear navigation.

#### Scenario: Next Button Behavior (NEW)
- **Given** the user is on Step 1
- **When** the user has NOT selected a date
- **Then** the "Continuar con la reserva" button MUST be disabled.
- **When** the user selects an available date
- **Then** the "Continuar con la reserva" button MUST be enabled.

#### Scenario: Back Button Behavior (NEW)
- **Given** the user is on Step 2
- **When** the user clicks "Volver"
- **Then** the `currentStep` MUST revert to 1.
- **And** all data already entered in the form MUST remain in the store.
- **And** the previously selected date MUST remain selected on the calendar.
