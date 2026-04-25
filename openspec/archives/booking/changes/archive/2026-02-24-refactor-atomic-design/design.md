# Design: Atomic Design Refactor and Cleanup

## Architectural Reasoning
The refactor transitions the codebase to a hierarchical component model and cleans up unused boilerplate.

### Mapping Logic
1.  **Atoms**: These are the basic building blocks. They are highly reusable and typically don't depend on other components (except other atoms).
    - Mapping: `src/components/ui/*` -> `src/components/atoms/ui/*`.
    - *Cleanup*: `src/components/Welcome.astro` will be DELETED.

2.  **Molecules**: Simple groups of atoms that function together as a unit. They should be relatively generic and reusable.
    - Mapping: `StatusLegend.tsx`, `StatusDetails.tsx` -> `src/components/molecules/`.

3.  **Organisms**: Complex components composed of molecules and atoms. They manage their own state, handle logic, or perform API calls. Since the current scope is primarily the booking feature, these components will live directly in `organisms/` for simplicity.
    - Mapping: `BookingCalendar.tsx`, `types.ts` -> `src/components/organisms/`.

## Implementation Details

### File Structure
```
src/components/
├── atoms/
│   └── ui/ (button, badge, etc.)
├── molecules/
│   ├── StatusDetails.tsx
│   └── StatusLegend.tsx
└── organisms/
    ├── BookingCalendar.tsx
    └── types.ts
```

### Path Aliases
We will ensure consistent use of the `@/components/...` alias to point to the new structure.

## Trade-offs
- **Flat Organisms**: Placing booking components directly in `organisms/` is simpler for now, but as new unrelated organisms are added (e.g., `ToursList`), sub-folders like `organisms/booking/` may be reintroduced to maintain organization.
- **Import Changes**: All imports across the project must be meticulously updated.
