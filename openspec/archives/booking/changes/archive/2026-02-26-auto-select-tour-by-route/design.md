# Design: Auto-select Tour by Route

## Overview
The goal is to enable tour-specific pages where the "Tour" field in the booking form is automatically pre-selected based on the URL path. Additionally, we want to ensure the routing is scalable and automatically updates when new tours are added to the data source.

## Architectural Decisions

### 1. Dynamic Routing in Astro
We will implement a dynamic route `src/pages/[id].astro`. 
- This page will use `getStaticPaths()` to generate routes for every tour defined in `src/data/tours.json`.
- The `id` parameter will correspond to the `id` field of the tour in the JSON.
- This ensures that adding a new tour to the JSON automatically creates a new page for it.

### 2. State Initialization via Props
To synchronize the routing state with the React-based booking form:
- The `BookingForm` component will be updated to accept an `initialTourId` prop.
- Inside `BookingForm`, a `useEffect` hook will detect if `initialTourId` is provided and update the Zustand store (`useBookingStore`) accordingly on mount.
- This ensures that the form state is consistent with the page the user is visiting.

### 3. Home Page Consistency
The existing `index.astro` will remain as the landing page. It can either:
- Keep the current behavior (no default selection).
- Or we could potentially add query parameter support (e.g., `/?tour=id`) to allow auto-selection on the home page as well, though the primary requirement is path-based routing. For now, we will focus on path-based routing for specific pages.

## Data Flow
1. User visits `/[id]`.
2. Astro resolves the `id` from `tours.json`.
3. Astro renders `[id].astro`, passing `id` to `BookingForm`.
4. `BookingForm` (React) mounts, calls `updateFormData({ tourId: id })` in the store.
5. The select input in the form reflects the selected tour.

## Alternatives Considered
- **Direct Store Access in Astro**: Astro components run on the server, while the Zustand store is client-side. We cannot set the store state directly in the `.astro` file.
- **Client-side only routing**: We could use a catch-all route and handle everything on the client, but using Astro's static generation is better for SEO and performance.
