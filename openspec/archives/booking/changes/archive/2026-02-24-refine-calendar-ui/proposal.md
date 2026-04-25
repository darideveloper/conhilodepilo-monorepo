# Proposal: Refine Booking Calendar UI

This proposal outlines the refinements for the **Booking Calendar** component to improve its visual consistency, mobile responsiveness, and overall user experience.

## Why
1.  **Visual Consistency:** The current calendar hover state needs to align with the brand's charcoal palette for a more professional look.
2.  **Responsiveness:** The calendar is currently hidden on mobile devices, preventing mobile users from checking availability. It should be fully visible and adapt to the screen width.
3.  **UI Cleanup:** The "Booking Schedule" title is redundant as the context of the calendar is clear, and its removal will help save vertical space.

## What Changes
- **Hover State:** Update the calendar date cells to use `brand-charcoal` (or a derivative) on hover.
- **Mobile Responsiveness:** Update the container classes in `src/pages/index.astro` and `src/components/BookingCalendar.tsx` to ensure visibility on all screen sizes.
- **Header Cleanup:** Remove the `CardHeader` containing the "Booking Schedule" title and description from `src/components/BookingCalendar.tsx`.

## Goals
- Improve the aesthetic quality of the calendar with brand-consistent hover effects.
- Ensure 100% availability visualization across all device types.
- Simplify the UI by removing redundant headers.

## Scope
- Component: `src/components/BookingCalendar.tsx` (Hover styles, Header removal).
- Integration: `src/pages/index.astro` (Responsiveness and visibility).
- Styling: `src/styles/global.css` (Optional, if global hover state is needed).

## Success Criteria
- Calendar dates change to black (brand-charcoal) background on hover.
- Calendar is visible and properly sized on mobile devices.
- "Booking Schedule" title is no longer present.
- `openspec validate` passes.
