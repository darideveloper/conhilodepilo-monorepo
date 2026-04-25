# Design: @astrojs/react Integration

## Problem Statement
The project needs a way to build interactive UI components with React to handle more complex client-side interactions that are difficult to manage with Vanilla CSS or basic Astro scripts alone.

## Proposed Solution
Install and configure the official `@astrojs/react` integration, which provides seamless React support within Astro components.

## Technical Decisions

### Integration Configuration
- Use the `@astrojs/react` package version `^5.0.0` or higher to align with Astro v6 (currently installed: `^5.0.1`).
- Add `react()` to the `integrations` array in `astro.config.mjs`.

### TypeScript Configuration
- Set `jsx` to `"react-jsx"` to use the modern React JSX transform.
- Set `jsxImportSource` to `"react"` to ensure types are correctly resolved.

### Performance Considerations
- Astro's "islands architecture" should be leveraged: only use `client:*` directives for components that actually require client-side interactivity to minimize JavaScript bundle size.

## Alternatives Considered
- **Preact:** Lighter but slightly different API; React was chosen for its broader ecosystem and documentation.
- **Vue/Svelte:** Also valid, but React is the most common requirement for interactive components in this project's context.

## Trade-offs
- **Bundle Size:** Adding React increases the bundle size on pages where it is hydrated. This should be mitigated by only hydrating what is necessary.
- **Complexity:** Managing two frameworks (Astro and React) adds some development overhead.
