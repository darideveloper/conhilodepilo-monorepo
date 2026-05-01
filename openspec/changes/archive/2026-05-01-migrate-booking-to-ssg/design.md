# Design: Single-Page SSG Migration

## Architecture Overview
The architecture will transition from a multi-route SSR application to a **Single-Page Application (SPA)** served as a static site. 

### Simplified Routing
- **Old:** `booking.com/` (Index) and `booking.com/[id]` (Service Path).
- **New:** `booking.com/` (Universal Entry Point).
- **Logic:** Service selection is moved entirely to query parameters (e.g., `booking.com/?service=123`). This matches the current implementation in the `BookingFlow.tsx` component which already parses these parameters.

## Technical Details

### 1. Removal of Dynamic Routes
By deleting `src/pages/[id].astro`, we remove the dependency on `getStaticPaths`. This is a critical improvement because:
- **Build Decoupling:** The frontend build no longer needs to fetch the list of services from the API. The build becomes purely about the UI code.
- **Instant Updates:** New services added in Django will work immediately in the booking app via `?service=NEW_ID` without needing a redeploy of the frontend.

### 2. Static Build Process
Astro will generate a single `index.html`. All logic for fetching service details, availability, and configuration is handled by the `BookingFlow` React component after the page loads in the browser.

### 3. Environment Variable Injection
The `PUBLIC_API_URL` will be baked into the static Javascript during the build. Since this URL rarely changes (it's the endpoint for the Django API), this is the only hard build dependency.

## Trade-offs and Considerations

### Pros
- **Robustness:** Zero rebuilds required for content updates (services, pricing, etc.).
- **Simplicity:** The app is now just a few static files.
- **Consistency:** Aligns with how the Landing page integrates the booking app (iframes with query params).

### Cons
- **Direct Link SEO:** Direct links to the booking app (e.g., sharing a link to a specific service) will use query parameters (`?service=ID`) instead of clean paths (`/ID`). However, since the Landing page already provides clean paths and SEO for services, this is not a significant loss.
