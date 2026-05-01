# Design: Unify Phone Configuration

## Architecture

The `landing` project is built with Astro. To fetch dynamic configuration data, we will utilize Astro's server-side fetching during the build (for static pages) or request (if SSR is enabled).

### 1. API Client Extension (with Caching)
We will add `getConfig.ts` to `landing/src/lib/api/`. Following the existing pattern in `client.ts`, this utility will use a module-level variable to cache the API response. 

**This ensures that even if multiple components (Layout, Footer, Page) call `getConfig()`, only one network request is made during the build or request lifecycle.**

### 2. Phone Formatting Utility
A new utility `landing/src/utils/phone.ts` will be created to handle two use cases:
*   `formatPhoneForWhatsApp(phone: string)`: Strips `+`, spaces, and dashes for `wa.me` links.
*   `formatPhoneForDisplay(phone: string)`: Ensures a consistent visual format (e.g., adding spaces for readability).

### 3. Component Refactoring (Simplified)

Instead of complex prop drilling, components will independently call the cached `getConfig()` utility. This keeps the components decoupled and the code cleaner, while maintaining high performance.

#### Footer & Layout
`Footer.astro` and `WhatsAppButton.astro` will internally call `getConfig()` to retrieve the data they need.

#### Booking Detail Page
`booking/[id].astro` will also call `getConfig()` for its specific WhatsApp CTA.

### 4. Sequence Diagram
1. `Layout.astro` calls `getConfig()`.
2. `Layout.astro` passes the `contact_phone` to `Footer` and `WhatsAppButton`.
3. `WhatsAppButton` uses `formatPhoneForWhatsApp` for the `href`.
4. `Footer` uses `formatPhoneForDisplay` for the visible text.

## Trade-offs
*   **Latency:** Fetching config on every page load (if SSR) or at build time. Given it's a small JSON, the impact is negligible.
*   **Static vs Dynamic:** If the site is purely static (`output: 'static'`), a rebuild is required when the phone changes in the dashboard. If SSR, it's real-time. We will assume the current project configuration (likely static with some islands).
