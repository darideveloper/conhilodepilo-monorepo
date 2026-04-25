# Proposal: Setup Brand Environment

This proposal outlines the setup of the project's visual identity based on the provided brand analysis for **Granada Go Tours**.

## Goals
- Integrate the brand's color palette and typography into the Tailwind CSS v4 configuration.
- Ensure the project follows the aesthetic of "Authority, Tradition, and Elegance".

## Scope
- **CSS Variables:** Define brand colors and font families in `src/styles/global.css`.
- **Typography:** Install and configure `@fontsource` packages for "Playfair Display" and "Lato".

## Success Criteria
- Colors `#A62C2B`, `#F9F7F2`, and `#2D2D2D` are accessible via Tailwind classes (e.g., `text-brand-red`, `bg-brand-cream`).
- "Playfair Display" is the default serif font and "Lato" is the default sans-serif font.
- `openspec validate` passes without errors.
