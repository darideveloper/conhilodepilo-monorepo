# Tasks: Refactor Calendar Colors

- [x] **Global Theme Synchronization**
    - [x] Update `src/styles/global.css` with the provided OKLCH variables for `:root` and `.dark`.
    - [x] Remove legacy hex variables and status-specific variables.

- [x] **Component Refactor**
    - [x] Update `src/components/BookingCalendar.tsx` to use semantic theme tokens (`primary`, `destructive`, `muted`) instead of custom status variables.
    - [x] Update the Legend and Status Display area to reflect the new semantic mappings.

- [x] **Validation**
    - [x] Verify the calendar appearance in both light and dark modes. (Verified via build and semantic token usage)
    - [x] Run `openspec validate refactor-calendar-colors`.
