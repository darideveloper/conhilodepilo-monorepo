# Change: Refactor Hero Component with React Slider

## Why
The current Hero component uses vanilla Swiper in an Astro script tag, which makes it harder to manage state and interactions. Refactoring it to a React component with `swiper/react` provides better integration with the React ecosystem and makes the component more robust and maintainable. Additionally, the user requested that the **entire Hero section** (both text and imagery) function as a single slide within the slider. Navigation links also need fixing to match existing section IDs, and the design should align with the HTML reference in `.themes/code.html`.

## What Changes
- **ADDED** `hero` capability spec to formally define Hero requirements for a full-section slider.
- **NEW** `src/components/HeroSlider.tsx` using `swiper/react` to manage the full-section slider.
- **MODIFIED** `src/components/HeroSection.astro` to delegate the entire rendering to the React slider.
- **FIX** Navigation links in the Hero section to ensure they point to existing section IDs (e.g., `#metodo` to `#info`).
- **UPDATE** Hero design to match the visual style of the `.themes/code.html` reference.

## Impact
- Affected specs: `hero` (new).
- Affected code: `src/components/HeroSection.astro`, `src/components/HeroSlider.tsx`.
- **BREAKING**: Replaces partial image-only slider with a full-section React Swiper implementation.
