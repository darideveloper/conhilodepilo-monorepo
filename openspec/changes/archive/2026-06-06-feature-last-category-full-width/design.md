## Context

The landing page displays service categories in a responsive grid. Currently all cards are identical in size and layout. The design goal is to give the last card a featured/full-width treatment to improve visual hierarchy and fill empty space on odd-card counts.

## Goals / Non-Goals

**Goals:**
- Last category card in showcase spans full grid width on tablet+ screens
- Last card uses horizontal layout with image constrained to 300px max-width
- Grid capped at 2 columns (removes 3-column breakpoint)
- Reuse existing `cn()` utility for conditional class composition
- Zero new dependencies

**Non-Goals:**
- No changes to card content, data fetching, or API layer
- No changes to mobile layout (all cards remain stacked)
- No animation or transition for the layout switch
- No configurable "featured" selection (always the last card)

## Decisions

- **Prop approach over CSS selector**: Using `isLast` prop instead of `:last-child` CSS pseudo-class because the component shouldn't need to know its position in the parent. The parent (`CategoryShowcase`) explicitly communicates the context.
- **`cn()` for conditional classes**: Follows existing codebase convention. No new class-merging utilities needed.
- **Removed 3-column grid**: With `md:col-span-2` on the last card, a 3-column grid would leave an overlap mismatch. Simplifying to 2-column grid avoids this and keeps the layout clean.
- **`md:max-w-[300px]` fixed width**: The horizontal layout needs a constrained image to prevent the image from taking half the viewport. 300px keeps it prominent but leaves ~60% width for the content section.

## Risks / Trade-offs

- [Odd card count edge case] → With exactly 2 cards on tablet, the last (2nd) card spans full width. This reduces the 2nd row to 1 item, which is an intentional trade-off for visual hierarchy.
- [1 card scenario] → A single category with `isLast` will span `md:col-span-2` on a 2-column grid, effectively full-width. This is the correct behavior for a featured layout.
- [No transition] → The layout switch between `flex-col` (mobile) and `flex-row` (tablet+) happens at the breakpoint boundary with no animation. Acceptable for current scope.
