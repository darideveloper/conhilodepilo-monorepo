# Design: Global Custom Scrollbar

## Architectural Approach
The scrollbar will be defined in the `@layer base` of `src/styles/global.css`. This ensures the styles apply globally to the browser's default scrollbar without requiring class changes on individual containers.

### Technical Details
- Use pseudo-elements: `::-webkit-scrollbar`, `::-webkit-scrollbar-track`, `::-webkit-scrollbar-thumb`.
- Mapping to design variables:
  - Track: `var(--color-ui-bg-light)`
  - Thumb: `var(--color-brand-primary)`
  - Hover: `var(--color-brand-secondary)`
  - Radius: `var(--radius-lg)`
- Border for thumb: `2px solid var(--color-ui-bg-light)` for contrast.
