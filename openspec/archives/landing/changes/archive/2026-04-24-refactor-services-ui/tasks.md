# Implementation Tasks

- [x] 1. **Update API Fetcher:** In `src/lib/api/getServices.ts`, add `getServiceCategories`. Also update `getServices` to use `svc.image || cat.image` so flattened services have valid images for the Design System.
- [x] 2. **Create CategoryCard:** Build `src/components/organisms/CategoryCard.tsx` using React. Mirror the `ServiceCard` visual structure (aspect ratio, styling). Use `useState` to default to the first service.
- [x] 3. **Create CategoryShowcase:** Build `src/components/organisms/CategoryShowcase.tsx` using a responsive CSS Grid.
- [x] 4. **Integrate into Homepage:** Update `src/pages/index.astro` to use `getServiceCategories` and render `<CategoryShowcase />`.
