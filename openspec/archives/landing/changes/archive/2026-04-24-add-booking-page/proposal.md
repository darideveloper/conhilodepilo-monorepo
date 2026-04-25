# Proposal: Add Dynamic Booking Page

This proposal introduces a new dynamic page `/booking/[id]` that allows users to view details of a specific service or course and proceed with booking via an embedded iframe.

## Problem
Currently, users can only see services and courses in sliders or lists on the home page. There is no dedicated page for a specific service where they can see more details and book directly.

## Solution
Create a new Astro page at `src/pages/booking/[id].astro` that fetches service or course data by ID from the backend and displays it in a premium, branded layout.

### Key Features
- **Dynamic Routing**: Use `[id].astro` to handle various services and courses.
- **Backend Integration**: Reuse existing API clients to fetch data.
- **Two-Column Layout**: 
  - Left: Service details (Title, Description, Image, CTAs).
  - Right: Booking iframe with `pre-selected` parameter.
- **Branding**: Strict adherence to existing design tokens and components.

## Scope
- `src/lib/api/getBookableItem.ts`: New helper to fetch a service or course by ID.
- `src/pages/booking/[id].astro`: New page component.
- Update `src/components/molecules/ServiceCard.astro` and `src/components/molecules/CourseCard.astro` to link to the new page (optional but recommended).

## Alternatives Considered
- **Modals**: Could use modals for booking, but a dedicated page is better for SEO and sharing.
- **Client-side only fetching**: Could use React for the whole page, but Astro is preferred for performance and SEO.
