# Proposal: Integrate Services API

## Goal
Replace the mocked dummy data API layer with real data fetched from the `[API_URL]/api/services/` endpoint, adhering to the structure defined in the `frontend-servcies-api.md` documentation.

## Problem
Currently, `getServices` and `getCourses` return static, hardcoded data with mocked types. The backend provides a single endpoint returning a nested array of `ServiceCategory` objects, where the first category represents courses and the subsequent categories represent services.

## Scope
- Update `src/lib/api/types.ts` to reflect the backend's `ServiceCategory` and `Service` interfaces.
- Modify `src/lib/api/getServices.ts` (or create a unified fetcher) to fetch from `PUBLIC_API_URL`.
- Refactor data mapping so the first category becomes the `courses` payload, and the rest are flattened into the `services` payload.
- Update `CourseCard.astro` to format numeric durations (minutes) to hours/days.
- Remove the Course Level Badge from `CourseCard.astro`.
- Render Markdown descriptions using the `marked` library.
- Update `ServiceCard.tsx`/`ServicesSlider.tsx` to format numeric durations and handle absolute image URLs.
- Configure `astro.config.mjs` to whitelist the backend domain for image optimization, reading the domain dynamically from the `PUBLIC_API_URL` environment variable with a fallback to `localhost:8000`.
