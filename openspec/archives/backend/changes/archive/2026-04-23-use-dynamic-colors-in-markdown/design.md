# Design: Dynamic Markdown Theming

## Color Mapping Strategy
To ensure the Markdown editor feels native to Unfold, we will map the elements to the following variables:

| Element | Target Variable |
|---------|-----------------|
| H1/H2 Borders | `var(--color-base-200)` |
| Blockquote Border | `var(--color-base-200)` |
| Blockquote Text | `var(--color-font-subtle-light)` |
| Code BG | `var(--color-base-100)` |
| Links | `var(--brand-primary-600, var(--color-primary-600))` |


## Implementation
The CSS in `static/css/style.css` will be updated to prioritize these variables. Fallback values will be kept only where necessary to prevent total styling loss if a variable is missing.

## Verification
The primary check is ensuring that `var(--brand-primary-600)` correctly inherits the color defined in the `CompanyProfile`.
