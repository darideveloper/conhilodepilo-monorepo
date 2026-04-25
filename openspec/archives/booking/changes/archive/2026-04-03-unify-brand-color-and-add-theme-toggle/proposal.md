# Proposal: Unify brand color and add light/dark theme toggle

## Summary
This change aims to consolidate the project's visual identity by using a single source-of-truth brand color across all UI components and implementing a theme switcher to allow users to toggle between light and dark modes.

## Problem
Currently, the branding uses multiple variables that, while related, are defined separately. Additionally, although dark mode variables are defined in the CSS, there is no user-accessible way to toggle between themes. The status colors in the calendar also diverge from the brand color palette, using standard Tailwind semantic colors instead.

## Solution
1. **Unify Brand Color:** Redefine the brand color variables to derive from a single primary brand color (Brand Red) in `global.css`.
2. **Harmonize Status Colors:** Update `STATUS_CONFIG` to use tones of the brand color or complementary shades that feel more integrated with the brand identity while maintaining semantic clarity.
3. **Theme Switcher:** Implement a React component to toggle the `.dark` class on the `<html>` element and persist the preference in `localStorage`.
4. **Shadcn/UI Sync:** Ensure all Shadcn/UI mappings in `global.css` correctly respond to theme changes.

## Scope
- `src/styles/global.css`: Redefining variables and theme mappings.
- `src/components/organisms/types.ts`: Updating `STATUS_CONFIG` colors.
- `src/components/atoms/ui/ThemeToggle.tsx`: New component for theme switching.
- `src/layouts/Layout.astro`: Adding the logic to apply the theme on load.
- `src/components/organisms/BookingFlow.tsx`: Adding the `ThemeToggle` to the UI.

## Dependencies
- None.
