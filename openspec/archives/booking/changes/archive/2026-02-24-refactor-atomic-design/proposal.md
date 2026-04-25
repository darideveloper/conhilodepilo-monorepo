# Proposal: Implement Atomic Design Structure

This proposal outlines the refactoring of the `src/components` directory to follow Atomic Design principles, categorizing components into Atoms, Molecules, and Organisms, and cleaning up unused components.

## Why
As the project grows, a flat or loosely organized component structure becomes difficult to maintain. Atomic Design provides a clear hierarchy that improves reusability, discoverability, and architectural consistency. Removing unused boilerplate components simplifies the codebase.

## What Changes
- **Directory Restructuring**: Create `atoms/`, `molecules/`, and `organisms/` directories under `src/components/`.
- **Component Removal**: Delete the unused `src/components/Welcome.astro` component and its import in `src/pages/index.astro`.
- **Component Migration**:
    - **Atoms**: Move shadcn/ui components (`badge`, `button`, `calendar`, `card`) to `atoms/ui/`.
    - **Molecules**: Move `StatusLegend` and `StatusDetails` to `molecules/`.
    - **Organisms**: Move `BookingCalendar` and its configuration `types.ts` directly into `organisms/`.
- **Import Resolution**: Update all internal and external imports to reflect the new paths.
- **Path Aliases**: Ensure `tsconfig.json` aliases are updated or used correctly to support the new structure.

## Goals
- Establish a scalable component architecture.
- Clearly distinguish between primitive components, composite components, and logic-heavy organisms.
- Improve developer experience by removing unused boilerplate and providing a clean structure.

## Scope
- Directory: `src/components/`.
- Usages in: `src/pages/`, `src/components/`, and any other file importing these components.

## Success Criteria
- All components are correctly categorized according to the proposed mapping.
- The `Welcome.astro` component is removed and no longer imported.
- The application builds and runs without import errors.
- `openspec validate` passes.
