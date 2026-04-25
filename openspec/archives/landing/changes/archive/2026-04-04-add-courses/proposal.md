# Change: Add Courses Section

## Why
The website needs a section showcasing the "Formación Exclusiva: Cursos Presenciales" to highlight the academy aspect of the brand. We must adapt the static HTML design provided in `.themes/code.html` to our Astro-based modular component system, downloading and optimizing the specific course imagery for local serving.

## What Changes
- Create `src/components/CourseCard.astro` to encapsulate the individual course display logic.
- Create `src/components/CoursesSection.astro` utilizing the global `<SectionHeader />` component and rendering the grid of course cards.
- Download the 3 external images from the HTML mockup into `src/assets/images/courses/` to leverage Astro's native `<Image />` optimization.
- Insert the `<CoursesSection />` into the homepage `index.astro`.

## Impact
- Affected specs: `courses` (new capability)
- Affected code: `src/components/CoursesSection.astro`, `src/components/CourseCard.astro`, `src/assets/images/courses/`, `src/pages/index.astro`
