# Design: Services API Integration

## Context
The backend exposes `/api/services/` returning a list of `ServiceCategory` objects. The frontend needs to split this single response into Courses (index 0) and Services (index 1+).

## Architecture Decisions

### 1. Unified Data Fetcher
Instead of performing duplicate HTTP requests to the same endpoint during the build or client hydration, we will create a cached/memoized fetcher in `src/lib/api/` that makes the network request once. Both `getCourses()` and `getServices()` will call this core function and map the resulting array accordingly.

### 2. Markdown Rendering
We will use a lightweight markdown parser (like `marked`) to render the descriptions returned by the API, as they contain bolding and line breaks. This will be integrated securely inside Astro components using `set:html`.

### 3. Image Handling
Images are returned as absolute URLs (e.g., `http://localhost:8000/...`). We will update Astro's `image.remotePatterns` configuration in `astro.config.mjs` to allow remote domains to be optimized by Astro's built-in image service.
