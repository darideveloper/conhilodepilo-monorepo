# Tasks: Atomic Design Refactor and Cleanup

- [x] **Scaffolding**
    - [x] Create `src/components/atoms/ui/` directory.
    - [x] Create `src/components/molecules/` directory.
    - [x] Create `src/components/organisms/` directory.

- [x] **Cleanup**
    - [x] Delete `src/components/Welcome.astro`.
    - [x] Remove `Welcome` import and usage in `src/pages/index.astro`.

- [x] **Migration: Atoms**
    - [x] Move shadcn components (`src/components/ui/*`) to `src/components/atoms/ui/`.
    - [x] Update internal imports within shadcn components (e.g., `calendar.tsx` imports from `button.tsx`).

- [x] **Migration: Molecules**
    - [x] Move `src/components/booking/StatusLegend.tsx` and `src/components/booking/StatusDetails.tsx` to `src/components/molecules/`.

- [x] **Migration: Organisms**
    - [x] Move `src/components/booking/BookingCalendar.tsx` and `src/components/booking/types.ts` to `src/components/organisms/`.

- [x] **Refactoring: Path Resolution**
    - [x] Update import path for `BookingCalendar` in `src/pages/index.astro`.
    - [x] Update internal imports within all moved components to match the new structure.

- [x] **Validation**
    - [x] Run `npm run build` to ensure no import/type errors.
    - [x] Verify that the `BookingCalendar` still renders and functions correctly.
    - [x] Run `openspec validate refactor-atomic-design`.
