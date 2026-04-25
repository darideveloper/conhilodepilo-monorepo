# Proposal: Auto-select Tour by Route

## Why
Currently, users have to manually select the tour they are interested in, even if they arrive at the site from a specific tour link. Providing tour-specific pages (e.g., `/alhambra-completa`) improves user experience and allows for better marketing of individual tours.

## What Changes
- **Store**: No changes needed to `useBookingStore.ts` as `updateFormData` already supports setting `tourId`.
- **UI Components**:
    - Update `BookingForm.tsx` to accept an `initialTourId` prop and initialize the store state on mount.
- **Routing**:
    - Create `src/pages/[id].astro` to handle tour-specific paths dynamically based on `src/data/tours.json`.

## Impact
- **New Routes**: Every tour ID in `tours.json` will now have a dedicated URL.
- **Form Behavior**: Visiting a tour-specific URL will pre-fill the "Tour" field in the booking form.
- **Scalability**: Adding a new tour to `tours.json` will automatically create its page and support auto-selection.
