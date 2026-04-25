# Spec: Brand Configuration

This spec defines the visual identity configuration for the Granada Go Tours project.

## ADDED Requirements

### Requirement: Visual Identity Tokens
The project SHALL have a consistent visual identity including colors and typography as defined in the brand analysis.

#### Scenario: Define Brand Colors
- Given the hex codes: Red (`#A62C2B`), Cream (`#F9F7F2`), Charcoal (`#2D2D2D`).
- When these are defined as CSS variables in the Tailwind `@theme` block.
- Then they MUST be available as Tailwind utility classes (e.g., `bg-brand-red`, `text-brand-charcoal`).

#### Scenario: Configure Typography
- Given the fonts: `Playfair Display` (Serif) and `Lato` (Sans-Serif).
- When Fontsource packages are installed and imported.
- Then `font-serif` MUST resolve to Playfair Display and `font-sans` to Lato.
