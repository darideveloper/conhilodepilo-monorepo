# Design: Dynamic Client-Side URL Adaptation

## Overview
Because Astro generates static pages, viewport-dependent values cannot be accurately determined on the server. The client-side injection pattern ensures correctness without violating static generation constraints.

## Patterns
- **Identifier:** Assign `id="booking-iframe"` to the existing iframe.
- **Script:** Inject an inline `<script>` tag at the end of the `[id].astro` component that:
  1. Selects the iframe by ID.
  2. Detects `window.innerWidth`.
  3. Calculates the appropriate zoom.
  4. Appends/updates the `&zoom=X` parameter on the `src`.
- **Performance:** Execute the script immediately upon DOM load to minimize iframe flickering/reloads.

## Trade-offs
- Slight chance of iframe reload (if src is updated after initial load), though setting the src dynamically in a `DOMContentLoaded` listener is generally efficient for modern browsers.
