## Context

The booking Step 1 component (`BookingServiceSelection.tsx`) renders three child divs inside a `flex-col` container within `CardContent`. Currently the DOM order matches the visual order: Selection Area → Stack/Cart Area → Continue button. Reordering requires only CSS because the parent is a flex container.

## Goals / Non-Goals

**Goals:**
- Visually place the Stack/Cart Area above the Selection Area on Step 1
- Preserve DOM order so tab navigation (accessibility) is unchanged
- Zero behavioral or JS logic changes

**Non-Goals:**
- No restructuring of React component hierarchy
- No changes to state management (Zustand store)
- No changes to other steps of the booking flow

## Decisions

- **Approach: CSS `order` on flex children** — The parent `CardContent` uses `flex flex-col`. Applying `order-1` to the cart div and `order-2` to the selection div reorders them visually. The button gets `order-3` to keep it last. Tailwind `order-{n}` maps to `order: n` in CSS.
- **Alternatives considered:**
  - **DOM reorder** — Moving the JSX directly would change tab order (screen readers would tab cart before dropdowns), requiring `tabIndex` management. More invasive.
  - **`flex-col-reverse`** — Would reverse all children including the button, requiring counter-ordering. More confusing.
  - **CSS Grid** — Possible but heavier; flex `order` is the simplest tool for this job.

## Risks / Trade-offs

- **[Confusion during maintenance]** → The DOM order no longer matches visual order. Mitigation: add a brief comment near the affected divs explaining they're reordered via `order`.
- **[order property browser support]** → `order` has 99.8%+ global support (since IE11). No risk for modern browsers.
