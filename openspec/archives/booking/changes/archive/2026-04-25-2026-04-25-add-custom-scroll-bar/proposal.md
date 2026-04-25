# Proposal: Add Custom Brand-Colored Scroll Bar

## Why
The application currently uses the browser default scroll bar, which can look jarring against the dynamic brand colors. By tying the scroll bar's appearance to the `brand_color` CSS variable, we can enhance the overall polish and "alive" feeling of the application as requested.

## What Changes
This proposal introduces a custom scroll bar design that utilizes the project's dynamic `brand_color`. This will ensure visual consistency across the entire application, as the scroll bar will now match the primary brand color used in buttons, accents, and other UI elements.

## Impact
- **UI/UX:** Improves visual cohesion.
- **Scope:** Global CSS (`src/styles/global.css`).
- **Complexity:** Low; requires adding `::-webkit-scrollbar` styles.
