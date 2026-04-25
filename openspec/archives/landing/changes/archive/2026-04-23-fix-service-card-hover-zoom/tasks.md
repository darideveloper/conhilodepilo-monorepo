# Tasks: Fix Service Card Hover Zoom

- [x] **Modify `ServiceCard.tsx`**
  - Update the root `article` element to use `group/card` instead of `group`.
  - Update the image element to use `group-hover/card:scale-105` instead of `group-hover:scale-105`.
  - Validate: Ensure no other `group-hover` utilities exist that need updating.

- [x] **Modify `ServiceCard.astro`**
  - Mirror the changes from the React version to maintain consistency.
  - Update the root `article` element to use `group/card`.
  - Update the image element to use `group-hover/card:scale-105`.

- [x] **Modify `CourseCard.astro`**
  - Update the root `div` element to use `group/card`.
  - Update the image element to use `group-hover/card:scale-105`.

- [x] **Manual Verification**
  - Run the dev server.
  - Navigate to a page with the `ServicesSlider`.
  - Hover over the slider area and individual cards to verify the zoom effect is isolated.
