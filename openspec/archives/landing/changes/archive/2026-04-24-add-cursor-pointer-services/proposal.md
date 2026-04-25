# Proposal: Add Cursor Pointer and Booking Redirect

## Goal
Improve the user experience by adding explicit `cursor-pointer` classes to all interactable elements and implementing a redirect logic for the `/booking` route to ensure users are correctly funneled through the service selection.

## Problem
1.  **UI Feedback:** The interactive elements in `CategoryCard` lack explicit pointer cursors.
2.  **Route Protection:** Accessing `/booking` without a specific service `id` leads to an empty or invalid state. Users should be redirected to the homepage to select a service first.

## Scope
- Add `cursor-pointer` to service selection buttons and CTA buttons in `CategoryCard.tsx`.
- Create `src/pages/booking.astro` to handle service booking.
- Implement logic in `booking.astro` to redirect to `/` if the `id` query parameter is missing or invalid.

## Out of Scope
- Implementing the full booking form logic (this proposal focuses on the routing and initial state).
