# Proposal: Compact Multi-Step Booking Flow

## Problem
The current booking interface displays both the form and the calendar simultaneously. This results in a cluttered UI, especially on smaller screens, and a vertically elongated form that feels unbalanced.

## Proposed Solution
Implement a **scalable, centralized multi-step booking system** that breaks the process into focused logical screens. This system will be managed via **Zustand**, providing a single source of truth for the current step and navigation logic.

### 1. Scalable Multi-Step System
- **Centralized Navigation**: All screen transitions will be handled by a new `currentStep` state in the `useBookingStore`.
- **Flexible Architecture**: The numeric step system allows for future expansion (e.g., adding a confirmation step or a pre-selection screen) without modifying core layout logic.
- **Progress Tracking**: A new step indicator (e.g., "1. Fecha" -> "2. Detalles") will provide visual feedback on the booking journey.

### 2. Guided Navigation ("Next" and "Back")
- **"Continuar con la reserva" (Next)**:
  - Appears in Step 1 (Calendar).
  - Remains disabled until a valid available date is selected.
  - Smoothly transitions the user to the personal details form.
- **"Volver" (Back)**:
  - Appears in Step 2 (Form).
  - Allows the user to return to the calendar to modify their date selection without losing any information already typed into the form.

### 3. Compact UI Enhancements
- **Focused Layout**: Instead of a split screen, the interface will center the active step's component, reducing visual noise and making the process feel more streamlined.
- **Responsive Field Grouping**: In Step 2 (Form), fields like "Name" and "Email" will be grouped into a single row on desktop (md+), significantly reducing vertical height.
- **Optimized Spacing**: Gaps and paddings will be tightened (from `gap-4` to `gap-3`) across all booking components.

## User-Visible Changes
- New "Next" and "Back" buttons for guided navigation.
- A progress indicator showing the current stage of the booking.
- A much more compact and focused form layout.
- Smooth transitions between the calendar and the form.

## Related Capabilities
- `booking-form`: Implements the compact layout and back navigation.
- `calendar`: Integrates the "Next" button and step validation.
- `state-management`: Centralizes the step-based flow in Zustand.
