# Design: Brand Color Unification and Theme Switching

## Architecture

### 1. Theme Toggle System
A React component, `ThemeToggle.tsx`, will handle user interaction to switch between light and dark themes.

#### Key Patterns:
- **Persistence:** Store the theme preference in `localStorage`.
- **Pre-load script:** A small blocking inline script in `Layout.astro`'s `<head>` will read `localStorage` and apply the `.dark` class immediately to prevent FOUC (Flash of Unstyled Content).
- **Tailwind v4 Synergy:** Leverage the existing `@theme` and `@layer base` structure in `global.css`.

### 2. Consolidated Brand Color
Instead of manually defining each OKLCH value separately, we will attempt to derive secondary and accent colors from the primary brand red (`oklch(0.577 0.245 27.325)`) where possible, or at least ensure they share the same hue.

#### Design Decisions:
- **Status Colors:** Currently, `STATUS_CONFIG` uses emerald, amber, and slate. We will shift these to maintain the same semantic meaning (green-ish for success, amber for warning, etc.) but using the OKLCH color space for better integration with the project's visual identity.
- **Dark Mode Primary:** Adjust the primary color lightness in dark mode to ensure high contrast and readability.

## Components & Changes

### CSS Variables
- **Primary:** `oklch(0.577 0.245 27.325)`
- **Background (Light):** `oklch(1 0 0)` (Pure white for cream)
- **Background (Dark):** `oklch(0.141 0.005 285.823)` (Charcoal)

### `ThemeToggle.tsx`
A simple button toggle using icons (Sun/Moon).

### `Layout.astro`
```html
<script is:inline>
  const theme = (() => {
    if (typeof localStorage !== 'undefined' && localStorage.getItem('theme')) {
      return localStorage.getItem('theme');
    }
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    return 'light';
  })();
  if (theme === 'dark') {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }
</script>
```

## Alternatives Considered
- **Theme via State Management (Zustand):** Decided against it to avoid unnecessary complexity for a simple CSS toggle.
- **Pure CSS (using `:has` and checkboxes):** Potential compatibility issues; React toggle is more flexible for future expansions (e.g., adding a "System" theme option).
