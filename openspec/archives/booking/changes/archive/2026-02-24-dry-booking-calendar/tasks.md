# Tasks: DRY BookingCalendar Refactor

- [x] **Data & Config Setup**
    - [x] Unify status keys: `booked`, `limited`, `available`, `standard`.
    - [x] Rename `bookingData` properties: `fullyBooked` -> `booked`, `limitedAvailability` -> `limited`.
    - [x] Define `STATUS_CONFIG` object with labels, icons, and color mappings (including `modifier` classes for the calendar).
    - [x] Define TypeScript types for status keys and config.

- [x] **Sub-component Implementation**
    - [x] Create `StatusLegend` component.
    - [x] Create `StatusDetails` component.

- [x] **Main Component Refactor**
    - [x] Integrate `STATUS_CONFIG` into `BookingCalendar`.
    - [x] Use `STATUS_CONFIG` to generate `modifiersClassNames` dynamically.
    - [x] Replace repetitive JSX in the main render function with sub-components.
    - [x] Optimize the `getStatus` logic to return unified status keys.

- [x] **Validation**
    - [x] Verify that all availability states still render correctly.
    - [x] Verify interactivity (date selection) still functions as expected.
    - [x] Run `openspec validate dry-booking-calendar`.
