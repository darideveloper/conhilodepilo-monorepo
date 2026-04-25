# Implementation Tasks

- [x] 1. **Setup API Layer:** Create the `src/lib/api` directory and define standard TypeScript interfaces (`Service`, `Course`) inside `src/lib/api/types.ts`.
- [x] 2. **Implement Courses API:** Create `src/lib/api/getCourses.ts` with an async function returning a mocked array of courses (using the existing hardcoded data, but formatted as an API response).
- [x] 3. **Implement Services API:** Create `src/lib/api/getServices.ts` with an async function returning a mocked array of services (migrating the JSON data from `src/content/services/`).
- [x] 4. **Refactor Courses UI:** Update `src/components/organisms/CoursesSection.astro` to remove the hardcoded array. Import and call `getCourses()` in the frontmatter. Update `CourseCard.astro` props if necessary.
- [x] 5. **Refactor Services UI (Astro):** Update `src/pages/index.astro` and `src/pages/design-system.astro` to remove `getCollection("services")`. Import and call `getServices()`.
- [x] 6. **Refactor Services UI (React):** Update `src/components/organisms/ServicesSlider.tsx` to accept the new flat `Service` interface instead of the Astro Collection shape. Update mapping logic accordingly.
- [x] 7. **Cleanup:** Delete `src/content/services` directory and remove the `services` collection schema from `src/content.config.ts`.
