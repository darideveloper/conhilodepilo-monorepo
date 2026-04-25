# Design: Scalable API Architecture

## Context
The project needs to scale beyond static content. We are establishing an API integration layer (`src/lib/api`) that will act as the single source of truth for dynamic data, isolating the components from the data-fetching implementation.

## Architecture Decisions

### 1. Dedicated API Layer
All data fetching will be abstracted into `src/lib/api/*.ts` files. Each domain (e.g., services, courses) will have its own file (e.g., `getServices.ts`, `getCourses.ts`). These scripts will mimic fetching from external HTTP endpoints.

### 2. UI Component Decoupling
Components (`ServicesSlider.tsx`, `CoursesSection.astro`) will receive flat data objects rather than Astro Collection objects. The API layer will be responsible for normalizing the data into standard TypeScript interfaces before passing them to the UI.

### 3. Error Handling and Resilience
The API functions will wrap their fetching logic in `try/catch` blocks. If the external dummy API fails, they should return empty arrays to prevent build crashes or client-side runtime errors.
