## MODIFIED Requirements
### Requirement: Form Initialization
The booking form MUST support initialization of its state via component properties.

#### Scenario: Initialize Tour ID
- **Given** the `BookingForm` is rendered with `initialTourId="alhambra-completa"`
- **When** the component mounts
- **Then** the `formData.selectedServices` array in the Zustand store MUST be initialized with "alhambra-completa".

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

#### Scenario: Display Multiple Services Summary
- **Given** the user is on Step 3 (Form)
- **When** the form renders
- **Then** it MUST display a summary of all services currently in the `selectedServices` array.
