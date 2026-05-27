## Context

The landing page header includes a "Sobre mí" nav link pointing to `/#info`, which anchors the `InfoCardSection`. The site owner wants only the header link removed — the section itself and other links (hero CTAs) should remain untouched.

Current state:
- **Header.astro**: `navLinks` array includes `{ label: "Sobre mí", href: "/#info" }`
- **HeroSection.astro**: Slides 1 and 3 have `secondaryCta` linking to `#info` — left unchanged
- **InfoCardSection.astro**: Renders `<section id="info">` — left unchanged

## Goals / Non-Goals

**Goals:**
- Remove the "Sobre mí" link from the header navigation
- Keep all other references to `#info` (hero CTAs, InfoCardSection) intact

**Non-Goals:**
- Removing or modifying the InfoCardSection
- Removing or modifying hero CTA buttons
- Redesigning the header layout or remaining nav links

## Decisions

**1. Remove only the header nav link, preserve everything else**

Rationale: The section is still valuable and reachable via in-page CTAs. Removing just the header link simplifies top-level navigation without eliminating content access.

Alternative considered: Remove the section entirely — rejected per user's explicit request to keep the section and other links.

## Risks / Trade-offs

- **Discovery via header removed** → Users can no longer find the info section through the top nav, but can still reach it via hero buttons and direct URL. This is the intended trade-off.