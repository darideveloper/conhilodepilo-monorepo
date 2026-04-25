# Proposal: Two-Step Service Selection

Implement a new initial screen for service selection (Service Type -> Service) before the calendar screen. This transforms the booking flow into a 3-step process and updates the data structure to support categorization.

## Goals

*   Create a new screen (`BookingServiceSelection`) as Step 1 of the booking flow.
*   Move the service selection out of the calendar into this new dedicated screen, using two dependent dropdowns (Service Type -> Service).
*   Transform the booking flow from a 2-step to a 3-step process (Selection -> Calendar -> Form).
*   Ensure the state management and routing correctly handle the new nested structure and step sequence.
*   Maintain existing branding from the API, global background, and overall layout (using `BookingHeader`, etc.).
*   Update translations to reflect the new 3-step sequence.
*   Use dummy data for all services.

## Scope

*   `src/data/booking.json`: Update to a categorized structure with dummy data.
*   `src/pages/api/tours.ts`: Remove this file entirely, as the API is deprecated.
*   `Codebase Imports`: Update all `tours.json` imports to `booking.json` across components, store, and pages.
*   `src/store/useBookingStore.ts`: Update to support `serviceTypeId` and handle nested data lookup.
*   `src/components/organisms/BookingServiceSelection.tsx`: Create a new component for the first step.
*   `src/components/organisms/BookingCalendar.tsx`: Remove the single dropdown, as it is now handled in Step 1.
*   `src/components/organisms/BookingFlow.tsx`: Update to manage 3 steps instead of 2.
*   `src/components/organisms/BookingForm.tsx`: Update lookup logic for selected service.
*   `src/pages/[id].astro`: Update `getStaticPaths` to support the nested data structure.
*   `src/lib/i18n/translations.ts`: Add `step1Of3`, `step2Of3`, `step3Of3` and related text.

## Non-Goals

*   Implementing a new API for tours (data remains static JSON for now).
*   Changing the underlying booking submission process (except for data lookup).
*   Modifying the overall visual theme or branding logic.