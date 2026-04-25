# Proposal: Apply DRY to BookingCalendar

This proposal outlines the refactoring of the `BookingCalendar` component to apply DRY (Don't Repeat Yourself) principles, improve modularity, and reduce code duplication.

## Why
The current `BookingCalendar` component contains repetitive logic and UI structures, particularly in the status visualization (legend, icons, colors, and badges). This makes the component harder to maintain and extend. Centralizing this logic will improve readability and architectural integrity.

## What Changes
- **Status Configuration**: Introduce a centralized `STATUS_CONFIG` object as the single source of truth for all availability states, including calendar modifiers, icons, and status details.
- **Unified Status Keys & Data Normalization**: Standardize status keys (`booked`, `limited`, `available`, `standard`) across the data model and UI. Rename `bookingData` properties to align with these keys.
- **Sub-components**: Break down the component into smaller, focused functional components:
    - `StatusLegend`: Renders the availability key dynamically from the config.
    - `StatusDetails`: Renders the details of the selected date using the config.
- **Logic Optimization**: Refactor `getStatus` to use the unified keys and improve the efficiency of date matching.
- **Styling Consolidation**: Use the configuration object to dynamically apply Tailwind classes to the calendar, legend, and details sections, eliminating redundant ternary operators and template literals.

## Goals
- Reduce the line count of the main component.
- Improve maintainability by centralizing status-related data.
- Enhance modularity for future feature additions.

## Scope
- Component: `src/components/BookingCalendar.tsx`.

## Success Criteria
- The component functionality remains identical to the current implementation.
- All repetitive conditional logic for status icons, colors, and badges is removed.
- Sub-components are used for distinct UI sections (Legend, Details).
- `openspec validate` passes.
