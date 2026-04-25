# Proposal: Add Booking Form Fields

## Problem
The current booking interface only features a calendar for date selection. To complete a booking request, users need to provide additional information such as their name, email, number of guests, the specific tour they are interested in, and any special requests. Currently, these fields are defined in the Zustand store but not exposed in the UI.

## Proposed Solution
Introduce a booking form to the left of the calendar (on large screens) or above it (on mobile). This form will capture all necessary user data and sync it with the existing Zustand store.

### Key Changes
- **New UI Atoms:** Create reusable `Input`, `Label`, `Textarea`, and `Select` components in `src/components/atoms/ui/` following Shadcn UI patterns and Tailwind CSS v4.
- **New Molecule/Organism:** Create a `BookingForm` component that aggregates the input fields.
- **Layout Update:** Modify `BookingCalendar` (or create a parent `BookingWidget`) to display the form and calendar side-by-side on desktop.
- **State Integration:** Bind all form fields to the `useBookingStore` to ensure real-time updates.
- **Branding:** Apply `brand-red`, `brand-charcoal`, and `brand-cream` colors to the form elements to match the existing visual identity.

## Impact
- **User Experience:** Provides a complete booking flow in a single widget.
- **Consistency:** Uses established project patterns (Zustand, Tailwind v4, atomic design).
- **Functionality:** Enables the collection of all data required for a booking request.
