# Tasks: Refactor Landing Data Filtering

## 1. Environment Configuration
- [x] 1.1 Update `landing/.env.example` with `PUBLIC_COURSES_GROUP_ID` and `PUBLIC_SERVICES_GROUP_ID`.
- [x] 1.2 Update local `landing/.env` with appropriate values (Courses: 2, Services: 1).

## 2. Type Definitions
- [x] 2.1 Update `ServiceCategory` interface in `landing/src/lib/api/types.ts` to include `group_id: number`.

## 3. Refactor Data Fetching
- [x] 3.1 Refactor `getCourses` in `landing/src/lib/api/getCourses.ts` to find the category using `import.meta.env.PUBLIC_COURSES_GROUP_ID`.
- [x] 3.2 Refactor `getServices` and `getServiceCategories` in `landing/src/lib/api/getServices.ts` to filter using `import.meta.env.PUBLIC_COURSES_GROUP_ID`.

## 4. Validation
- [x] 4.1 Verify landing page rendering of Services section.
- [x] 4.2 Verify landing page rendering of Courses section.
- [x] 4.3 Ensure no regressions in data mapping (titles, prices, images).
