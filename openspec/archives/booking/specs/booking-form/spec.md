# booking-form Specification

## Purpose
TBD - created by archiving change add-booking-form-fields. Update Purpose after archive.
## Requirements
### Requirement: Form Field Sync
The booking form MUST synchronize all input values with the `useBookingStore`.

#### Scenario: Update Privacy Acceptance (NEW)
- **Given** the user is on Step 2 of the booking form
- **When** the user checks the "Acepto la política de privacidad" checkbox
- **Then** the `formData.privacyAccepted` in the Zustand store MUST be set to `true`

### Requirement: Visual Branding
All form elements MUST adhere to the project's brand color palette.

#### Scenario: Focus State
- **Given** an input field is focused
- **Then** its border or ring color MUST use the `brand-red` color.

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

### Requirement: Form Initialization
The booking form MUST support initialization of its state via component properties.

#### Scenario: Initialize Tour ID
- **Given** the `BookingForm` is rendered with `initialTourId="alhambra-completa"`
- **When** the component mounts
- **Then** the `formData.selectedServices` array in the Zustand store MUST be initialized with "alhambra-completa".

### Requirement: UI Simplification
The `BookingForm` SHALL NOT display step indicators.

#### Scenario: No Step Indicator in Step 2
- **Given** the user is on the `BookingForm`
- **Then** the text "Paso 2 de 2" MUST NOT be visible.

### Requirement: Form Submission Validation
The booking form MUST NOT allow submission without explicit user consent to the privacy policy.

#### Scenario: Submit Without Consent
- **Given** the user is on Step 2 of the booking form
- **And** the "Acepto la política de privacidad" checkbox is NOT checked
- **When** the user clicks "Solicitar Reserva"
- **Then** the browser SHOULD prevent submission via HTML5 validation
- **And** the application MUST NOT trigger the Stripe payment API call.

#### Scenario: Submit With Consent
- **Given** the user is on Step 2 of the booking form
- **And** the "Acepto la política de privacidad" checkbox IS checked
- **And** all other required fields are valid
- **When** the user clicks "Solicitar Reserva"
- **Then** the application MUST trigger the Stripe payment API call.

### Requirement: Privacy Policy Access
The booking form MUST provide a clear link to the privacy policy.

#### Scenario: External Link to Privacy Policy
- **Given** the user is on Step 2 of the booking form
- **When** the user clicks the "política de privacidad" link
- **Then** the browser SHOULD open `https://granadago.com/privacidad/` in a new tab.

