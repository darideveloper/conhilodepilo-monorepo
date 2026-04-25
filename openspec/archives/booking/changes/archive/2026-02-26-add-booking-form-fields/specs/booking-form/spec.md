# Capability: Booking Form

## ADDED Requirements

### Requirement: Form Field Sync
The booking form MUST synchronize all input values with the `useBookingStore`.

#### Scenario: Update Full Name
- **Given** the user is on the booking page
- **When** the user types "Juan Pérez" in the Full Name field
- **Then** the `formData.fullName` in the Zustand store MUST be updated to "Juan Pérez"

#### Scenario: Update Email
- **Given** the user is on the booking page
- **When** the user types "juan@example.com" in the Email field
- **Then** the `formData.email` in the Zustand store MUST be updated to "juan@example.com"

#### Scenario: Select Tour
- **Given** the user is on the booking page
- **When** the user selects "Alhambra Completa" from the Tour dropdown
- **Then** the `formData.tourId` in the Zustand store MUST be updated to "alhambra-completa"

### Requirement: Visual Branding
All form elements MUST adhere to the project's brand color palette.

#### Scenario: Focus State
- **Given** an input field is focused
- **Then** its border or ring color MUST use the `brand-red` color.

### Requirement: Responsive Layout
The booking interface MUST adapt its layout based on the screen size.

#### Scenario: Desktop Layout
- **Given** a screen width of 1024px or greater
- **Then** the booking form MUST be displayed to the left of the booking calendar.

#### Scenario: Mobile Layout
- **Given** a screen width less than 1024px
- **Then** the booking form MUST be displayed stacked with the booking calendar.
