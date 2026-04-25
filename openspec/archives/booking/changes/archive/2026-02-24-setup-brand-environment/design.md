# Design: Brand Environment Integration

## Architectural Reasoning
The project uses **Tailwind CSS v4**, which simplifies configuration by moving it into CSS variables using the `@theme` block. This aligns perfectly with the goal of defining brand tokens directly in the stylesheet while keeping them accessible to Tailwind's engine. 

All visual identity tokens will be centralized in `src/styles/global.css`.

### Typography Strategy
Using **Fontsource** is the standard for Astro/Vite projects as it provides self-hosted fonts, improving performance and privacy over Google Fonts CDN. 
- **Playfair Display**: Chosen for headings to convey the "historical and Mediterranean" feel.
- **Lato**: Chosen for body text for modern readability and mobile optimization.

### Color Mapping
- `primary`: `#A62C2B` (Pomegranate Red)
- `background`: `#F9F7F2` (Off-White/Cream)
- `text`: `#2D2D2D` (Deep Charcoal)
- `accent`: Beige/Earth tones derived from the palette.

## Implementation Details

### CSS Variable Mapping (Tailwind v4)
We will use the `@theme` block in `src/styles/global.css`:
```css
@theme {
  --color-brand-red: #A62C2B;
  --color-brand-cream: #F9F7F2;
  --color-brand-charcoal: #2D2D2D;
  
  --font-serif: "Playfair Display", serif;
  --font-sans: "Lato", sans-serif;
}
```

## Trade-offs
- **Self-hosted fonts vs CDN**: Self-hosting via Fontsource adds to the initial bundle size but guarantees availability and performance.
- **Pure CSS configuration**: By avoiding `.env` for styles, we maintain a single source of truth for design tokens within the styling layer, which is more idiomatic for Tailwind v4.
