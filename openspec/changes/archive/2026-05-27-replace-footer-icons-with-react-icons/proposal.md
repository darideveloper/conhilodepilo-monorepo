## Why

The footer currently uses `@lucide/astro` via a custom `Icon.astro` wrapper with a hand-crafted inline SVG fallback for TikTok. Since the project already has React 19 and `@astrojs/react` available, standardizing on `react-icons` eliminates a bespoke icon abstraction, removes the dependency on `@lucide/astro`, and provides first-class TikTok icon support without custom SVGs.

## What Changes

- Replace `Icon.astro` and all `@lucide/astro` usage with `react-icons` components
- Refactor the footer social link icons to use `react-icons`
- Remove the `@lucide/astro` dependency
- Add `react-icons` as a dependency
- Deprecate and remove the `Icon.astro` wrapper component

## Capabilities

### New Capabilities
- `react-icons-migration`: Migrate the landing page from `@lucide/astro` to `react-icons`, starting with the footer social icons as the initial scope.

### Modified Capabilities
<!-- No existing capability specs have requirement changes -->

## Impact

- **Dependencies**: Add `react-icons`, remove `@lucide/astro`
- **Components**: Remove `landing/src/components/atoms/Icon.astro`; update `landing/src/components/organisms/Footer.astro` to use React icons
- **Other consumers**: Any other component using `Icon.astro` will need migration
