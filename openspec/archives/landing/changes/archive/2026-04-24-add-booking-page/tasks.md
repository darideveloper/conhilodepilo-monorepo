# Tasks: Add Booking Page

## Implementation

- [x] Create `src/lib/api/getBookableItem.ts` helper
  - Validation: Unit test or manual check that it finds both services and courses.
- [x] Create `src/pages/booking/[id].astro`
  - [x] Implement `getStaticPaths` to pre-render all services and courses.
  - [x] Implement layout with `Layout` component.
  - [x] Implement Title, Description, and Image sections.
  - [x] Implement CTA section with WhatsApp button.
  - [x] Implement Iframe section with dynamic URL.
  - Validation: Visit `/booking/{id}` for several existing IDs and verify content.
- [x] Update `ServiceCard` and `CourseCard` to link to `/booking/{id}`
  - Validation: Clicking a card redirects to the correct booking page.

## Verification
- [x] Run `npm run build` to ensure static generation works for all paths.
- [x] Verify responsive behavior (mobile stack vs desktop side-by-side).
