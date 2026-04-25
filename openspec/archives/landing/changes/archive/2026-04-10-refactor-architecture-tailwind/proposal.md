# Change: Refactor Architecture and Styling

## Why
Currently the project's components structure is unorganized and styling inconsistently relies on Vanilla CSS alongside a newer Tailwind integration. Implementing an Atomic Design structure combined with a firm direction towards using only Tailwind CSS will improve consistency, reusability, and long-term project maintainability.

## What Changes
- Organize components using Atomic Design principles (`atoms/`, `molecules/`, `organisms/`).
- Force the adoption of Tailwind CSS for styling across components, removing custom scoped Vanilla CSS wherever practical.
- Update import paths systematically across layouts, pages, and components.

## Impact
- Affected specs: `architecture`, `tailwind`
- Affected code: `src/components/*`, `src/layouts/*`, `src/pages/*`
