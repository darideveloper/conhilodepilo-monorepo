# Design: Final SSG Refinements

## Client-Side Style Injection for Zoom
Since SSG pre-renders pages at build time, it cannot access URL parameters like `zoom` on the server. To preserve the iframe scaling functionality:
- A client-side script in `Layout.astro` reads `zoom` from `window.location.search`.
- It dynamically creates a `<style>` element and appends it to the `<head>`.
- This ensures the zoom is applied as soon as the body is created, avoiding layout shifts.

## Single-Page Static Routing
The project now uses a single `index.astro` entry point. All service-specific logic is handled by the `BookingFlow` React component parsing the `service` query parameter. This approach:
- Decouples the build from the backend API (no `getStaticPaths`).
- Allows new services to be used immediately without a redeploy.
- Simplifies the hosting requirements to a pure static server.
