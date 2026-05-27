## Context

The current landing page hero section uses lower quality, mixed-resolution images (`hero-treatments.webp`, `hero-academy.webp`, `hero-experience.webp`). We have new, uniform high-quality WebP assets ready in `landing/src/assets/images/` (`hero-1.webp`, `hero-2.webp`, `hero-3.webp`). 

## Goals / Non-Goals

**Goals:**
- Update `HeroSection.astro` to use the new images.
- Improve the visual quality of the hero carousel.
- Maintain existing slider layout and behavior.

**Non-Goals:**
- Redesigning the hero section layout.
- Adding new slides or changing text content.

## Decisions

- **Image Mapping**: We will map the specific images to the slides logically based on the content (Treatments -> hero-1, Academy -> hero-2, Experience -> hero-3).
- **Format**: We continue to use WebP for optimal performance.
- **Cleanup**: We will remove the old image imports to keep the codebase clean.

## Risks / Trade-offs

- **Risk**: New images might have different aspect ratios affecting the UI.
  - **Mitigation**: Verified via `identify` that all new images are exactly 800x1067, which ensures a consistent slider height and layout.
