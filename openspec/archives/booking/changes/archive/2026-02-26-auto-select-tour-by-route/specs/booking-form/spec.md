# Booking Form Specification

## ADDED Requirements

### Requirement: Form Initialization
The booking form MUST support initialization of its state via component properties.

#### Scenario: Initialize Tour ID
- **Given** the `BookingForm` is rendered with `initialTourId="alhambra-completa"`
- **When** the component mounts
- **Then** the `formData.tourId` in the Zustand store MUST be set to "alhambra-completa".
