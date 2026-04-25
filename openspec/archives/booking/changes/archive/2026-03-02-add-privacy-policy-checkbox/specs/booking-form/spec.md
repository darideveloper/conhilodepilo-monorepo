# Booking Form Specification Delta

## MODIFIED Requirements

### Requirement: Form Field Sync
The booking form MUST synchronize all input values with the `useBookingStore`.

#### Scenario: Update Privacy Acceptance (NEW)
- **Given** the user is on Step 2 of the booking form
- **When** the user checks the "Acepto la política de privacidad" checkbox
- **Then** the `formData.privacyAccepted` in the Zustand store MUST be set to `true`

## ADDED Requirements

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
