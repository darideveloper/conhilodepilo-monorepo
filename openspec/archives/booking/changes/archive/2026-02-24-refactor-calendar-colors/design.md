# Design: Unified OKLCH Brand Coloring

## Architectural Reasoning
We are adopting the **OKLCH** color space for the project's theme. OKLCH provides better perceptual uniformity and is the modern standard for Tailwind CSS v4. 

We will synchronize the `:root` and `.dark` blocks in `global.css` with the provided reference values and then map the calendar components to these semantic tokens.

### Theme Synchronization (OKLCH)
Key mappings from the reference:
- `background`: `oklch(1 0 0)` (White) / `oklch(0.141 0.005 285.823)` (Charcoal)
- `primary`: `oklch(0.577 0.245 27.325)` (Brand Red)
- `destructive`: `oklch(0.577 0.245 27.325)` (Brand Red)
- `ring`: `oklch(0.704 0.191 22.216)`

### Semantic Calendar Mapping
Instead of hardcoded colors, we will use the following semantic mappings:

| State | Theme Token | Effect |
| :--- | :--- | :--- |
| **Full** | `destructive` | Uses the Brand Red to indicate unavailability. |
| **Limited** | `muted` | Uses the secondary/muted charcoal for a subtle look. |
| **Available** | `primary` | Uses the Brand Red (or primary accent) to highlight opportunity. |

## Implementation Details

### CSS Update
We will replace the entire `:root` and `.dark` blocks in `src/styles/global.css` with the OKLCH values provided in the reference.

### Component Refactor
In `BookingCalendar.tsx`, the `modifiersClassNames` will be updated to use these semantic Tailwind classes:
- `booked`: `bg-destructive/10 text-destructive line-through opacity-50`
- `limited`: `bg-muted text-muted-foreground border-b-2 border-muted-foreground`
- `available`: `bg-primary text-primary-foreground font-bold`

## Trade-offs
- **Red for both Full and Available**: Since the Brand Red is the primary color, we must distinguish between "Actionable Red" (Available) and "Warning Red" (Full). We will use high contrast/solid fill for Available and low-opacity/strikethrough for Full.
