# Design: shadcn/ui Integration with Tailwind v4

## Architectural Reasoning
Shadcn/ui with Tailwind v4 adopts a **CSS-first** approach. Instead of a `tailwind.config.js`, we define theme variables directly in the CSS file. This aligns with the project's existing use of `@tailwindcss/vite`.

### Color Mapping for GranadaGo
To maintain the "Authority, Tradition, and Elegance" aesthetic, shadcn/ui variables will be mapped to the brand colors:

| shadcn variable | Brand Equivalent | Hex |
| :--- | :--- | :--- |
| `--background` | Cream | `#F9F7F2` |
| `--foreground` | Charcoal | `#2D2D2D` |
| `--primary` | Pomegranate Red | `#A62C2B` |
| `--primary-foreground` | Cream | `#F9F7F2` |
| `--secondary` | Charcoal | `#2D2D2D` |
| `--secondary-foreground` | Cream | `#F9F7F2` |
| `--muted` | Light Beige (derived) | `#E8E3D9` (approx) |
| `--accent` | Pomegranate Red (low opacity) | `#A62C2B` |

### Path Aliases
We use `@/*` mapping to `src/*` to avoid brittle relative imports (e.g., `../../components/ui/button`).

### Component Management
Components will be added to `src/components/ui`. Interactive components will be implemented as React components (using `client:load` or similar Astro directives when used in pages).

## Implementation Details

### tsconfig.json
Add `baseUrl` and `paths` to `compilerOptions`.

### components.json
Configure for Astro + Tailwind v4:
- `style`: `new-york`
- `baseColor`: `slate`
- `css`: `src/styles/global.css`
- `cssVariables`: `true`

### global.css
Utilize Tailwind v4 `@theme` block and define `:root` variables in HSL or OKLCH as expected by shadcn/ui components for better color manipulation (like transparency).
*Note: Although hex is easier, shadcn's internal utility patterns often benefit from HSL for hover states in some versions. For v4, we can use hex if we want, as v4 handles them well.*

### Utilities
The standard `cn` utility will be placed in `src/lib/utils.ts`.
