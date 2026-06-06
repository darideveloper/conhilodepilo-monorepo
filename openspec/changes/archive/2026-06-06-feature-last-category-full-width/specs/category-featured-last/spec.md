## ADDED Requirements

### Requirement: Last category card spans full grid width
The last `CategoryCard` in a `CategoryShowcase` SHALL span the full grid width on screens 768px and wider. The card container SHALL use `md:col-span-2` and `md:flex-row` classes when the `isLast` prop is true. The image wrapper SHALL have a max-width of 300px (`md:max-w-[300px]`) when `isLast` is true.

#### Scenario: Last card spans 2 columns on tablet+
- **WHEN** `CategoryShowcase` renders 3 categories on a screen >= 768px
- **THEN** the 3rd `CategoryCard` SHALL have `md:col-span-2` and `md:flex-row` classes applied, making it span both grid columns with horizontal layout

#### Scenario: Normal card does not span
- **WHEN** a `CategoryCard` has no `isLast` prop or `isLast` is `false`
- **THEN** the card SHALL render in normal column layout without `md:col-span-2`, `md:flex-row`, or `md:max-w-[300px]`

#### Scenario: Single category shows full-width
- **WHEN** `CategoryShowcase` renders exactly 1 category
- **THEN** the card SHALL have `isLast` as `true` and span the full 2-column grid width

### Requirement: Grid caps at 2 columns
The `CategoryShowcase` grid SHALL use `grid-cols-1 md:grid-cols-2` with no 3-column breakpoint. This ensures the last-card spanning behavior works consistently.

#### Scenario: No 3-column grid
- **WHEN** viewing the showcase on any screen size
- **THEN** the grid SHALL never exceed 2 columns at any breakpoint

#### Scenario: 2 cards on tablet
- **WHEN** there are exactly 2 categories on a screen >= 768px
- **THEN** the grid SHALL render 2 columns, with the last (2nd) card spanning both columns in horizontal layout
