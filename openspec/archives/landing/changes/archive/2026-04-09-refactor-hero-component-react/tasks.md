# Tasks: Refactor Hero Component with React Slider

Refactor the Hero component to use a React-based slider with `swiper/react` where the whole section (text + images) is part of the slider.

## 1. Spec Update
- [x] Update `openspec/changes/refactor-hero-component-react/specs/hero/spec.md` to specify a full-section slider.

## 2. Implementation
- [x] Refactor `src/components/HeroSlider.tsx` to handle full-section slides.
    - [x] Update props to accept full slide data (badge, title, accent, description, CTAs, image).
    - [x] Move the Hero layout (grid, left column content, right column imagery) inside `SwiperSlide`.
    - [x] Ensure proper responsive styling within each slide.
- [x] Update `src/components/HeroSection.astro`.
    - [x] Pass full slide data to `HeroSlider.tsx`.
    - [x] Clean up redundant layout code (moved to the React component).
- [x] Verify functionality.
    - [x] Test the full-section transition (text and image sliding together).
    - [x] Verify CTAs on all slides point to correct sections.

## 3. Cleanup
- [x] Remove `src/components/HeroSlider.astro` (already done).
- [ ] Archive the change after verification.
