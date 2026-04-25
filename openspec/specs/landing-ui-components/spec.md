# landing-ui-components Specification

## Purpose
TBD - created by archiving change fix-reacticon-hydration-landing. Update Purpose after archive.
## Requirements
### Requirement: React Components in Astro MUST use appropriate client directives
React components that rely on client-side lifecycle hooks (such as `useEffect` or `useState`) MUST be rendered with an appropriate Astro client directive (e.g., `client:load`, `client:visible`, or `client:idle`) when used within `.astro` files.

#### Scenario: ReactIcon component hydration
- **Given** a `ReactIcon` component is used in an `.astro` template
- **When** the component is rendered
- **Then** the `client:load` directive is present to ensure the component hydrates and its `useEffect` hook runs on the client to load the icon.

