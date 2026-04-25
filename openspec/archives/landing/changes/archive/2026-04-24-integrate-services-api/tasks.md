# Implementation Tasks

- [x] 1. **Environment Setup:** Add `PUBLIC_API_URL` to `.env.example` and `.env` (default to `http://localhost:8000`). Update `astro.config.mjs` to whitelist this domain for image optimization via `remotePatterns` by parsing the domain dynamically from the env variable.
- [x] 2. **Update Types:** Refactor `src/lib/api/types.ts` to include `ServiceCategory` and match the API's `Service` structure (`id` as number, `duration` as number, `image` as string).
- [x] 3. **Implement API Fetcher:** Update `src/lib/api/getServices.ts` and `getCourses.ts` (or unify them) to fetch from `${PUBLIC_API_URL}/api/services/`. Split the response: category `0` for courses, categories `1+` mapped to a flat array for services. Add error handling.
- [x] 4. **Refactor Courses UI:** Install the `marked` library. Update `CourseCard.astro` to format the numeric duration (e.g., converting 180 to "3 horas"). Parse the markdown description safely using `marked`. Remove the `level` badge entirely from the UI.
- [x] 5. **Refactor Services UI:** Update `ServiceCard.astro` and `ServiceCard.tsx` to format numeric durations (e.g., appending " min") and handle remote image URLs instead of static imports.
- [x] 6. **Update Slider Logic:** Update `ServicesSlider.tsx` sorting and mapping logic since the `order` property is removed. Rely on the API's natural order.
