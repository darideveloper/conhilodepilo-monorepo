# Design: Tailwind CSS v4 Installation

Tailwind CSS v4 introduces a more streamlined setup in Astro, primarily leveraging `@tailwindcss/vite` instead of a dedicated Astro integration for styling rules, although the `@astrojs/tailwind` integration still handles the CLI experience for installation and some configuration.

## Architectural Reasoning

### Official Integration

The `npx astro add tailwind` command is the recommended way to get started. In Astro >= 5.2.0, this command should automatically set up the Tailwind v4 Vite plugin.

### Global Stylesheet

Tailwind v4 recommends a CSS-first approach where `@import "tailwindcss";` is used in a global CSS file. This file must then be imported in a high-level layout or page component to be available globally.

## Implementation Details

### Dependencies
- `@tailwindcss/vite` (likely installed by `astro add tailwind`)
- `tailwindcss` (version 4)

### Entry Point
- `src/styles/global.css`: The central location for Tailwind's `@import` and any global custom styles or theme variables.

### Layout Integration
- `src/layouts/Layout.astro`: This layout will import the `global.css` file to ensure Tailwind is loaded for all pages that use this layout.
