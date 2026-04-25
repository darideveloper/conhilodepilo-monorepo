# Design: Hero Component Refactor (Full-Section Slider)

## Context
The project is built with Astro and uses React for interactive components. Originally, only the image was a slider. The updated requirement is to make the entire Hero section (text content + imagery) slide together.

## Goals
- Refactor `HeroSlider.tsx` to encapsulate the entire Hero section layout within each slide.
- Use `swiper/react` to manage transitions for the entire grid (content and imagery).
- Ensure CTAs remain functional and fixed navigation targets are used.
- Align with the visual identity from `.themes/code.html`.

## Decisions

### Decision: Full-Section Slide Layout
- Each `SwiperSlide` will contain the full responsive grid (left column for text, right column for imagery).
- This ensures that when a slide changes, all information relevant to that slide transitions simultaneously.

### Decision: Data Structure
- The `HeroSlider` will accept an array of slide objects, each containing:
  - `badge`, `title`, `titleAccent`, `description`, `primaryCta`, `secondaryCta`, `image`, `imageAlt`.

### Decision: Component Responsibility
- `HeroSection.astro` will now mainly serve as a data provider and a container for the React component. All layout within the Hero section is delegated to the React slider to ensure consistent behavior across slides.

## Risks / Trade-offs
- **Complexity**: Managing the entire section layout within React means we need to ensure all Tailwind utilities and project-specific classes are correctly applied in the JSX.
- **SSR/Hydration**: The entire section will be client-side rendered/hydrated. This is necessary for the slider functionality but should be monitored for CLS (Cumulative Layout Shift).
