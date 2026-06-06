## Why

The category showcase grid currently displays all service categories as uniform cards in a 3-column layout. On medium-to-large screens, this leaves an awkward empty space when the number of categories is odd (e.g., 2, 4 cards), and all cards look identical — there is no visual hierarchy to guide the user's attention. By making the last category card span the full grid width with a horizontal layout, we create a natural visual anchor that improves readability and screen utilization.

## What Changes

- **`CategoryCard`**: Accept new `isLast` boolean prop. When true, the card spans 2 grid columns (`md:col-span-2`) and switches to horizontal flex layout (`md:flex-row`). The image area gets a fixed max-width (`md:max-w-[300px]`) instead of filling the full card width.
- **`CategoryShowcase`**: Remove `lg:grid-cols-3` from the grid definition (capped at `md:grid-cols-2`). Pass `isLast={index === categories.length - 1}` to the last rendered `CategoryCard`.
- **Grid column reduction**: The grid no longer supports a 3-column breakpoint — it transitions directly from 1 column (mobile) to 2 columns (tablet/desktop). This ensures the last-card spanning behavior works cleanly across all viewports.

## Capabilities

### New Capabilities
- `category-featured-last`: Last category in the showcase receives a featured/full-width treatment with horizontal layout and constrained image size, creating visual hierarchy.

### Modified Capabilities

None — no existing specs are modified.

## Impact

- **Files modified**: `landing/src/components/organisms/CategoryCard.tsx`, `landing/src/components/organisms/CategoryShowcase.tsx`
- **Grid behavior**: Removed `lg:grid-cols-3` — categories will never display in 3 columns. On screens >= 768px, an odd number of cards will show the last one spanning full width horizontally.
- **No API/dependency changes**: Pure UI change within the landing page component layer.
