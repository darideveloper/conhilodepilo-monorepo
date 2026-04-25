# Tasks: Unify brand color and add light/dark theme toggle

## Refactor
- [x] Redefine brand colors in `src/styles/global.css` using a single source of truth for the primary red. <!-- id: 1 -->
- [x] Harmonize status colors in `src/components/organisms/types.ts` to use brand-consistent OKLCH colors. <!-- id: 2 -->

## Feature
- [x] Implement `ThemeToggle.tsx` component to handle theme switching and persistence in `localStorage`. <!-- id: 3 -->
- [x] Add the pre-load script to `src/layouts/Layout.astro` to apply theme on page load. <!-- id: 4 -->
- [x] Integrate `ThemeToggle` into `src/components/organisms/BookingFlow.tsx`. <!-- id: 5 -->

## Validation
- [x] Verify light and dark mode appearance across all UI components. <!-- id: 6 -->
- [x] Ensure theme preference persists across page reloads. <!-- id: 7 -->
- [x] Confirm single brand color consistency in all primary buttons and UI elements. <!-- id: 8 -->
