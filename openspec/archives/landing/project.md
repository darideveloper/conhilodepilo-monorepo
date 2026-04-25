# Project Context

## Purpose
Con Hilo Depilo is a web project built with Astro, likely for a hair removal service (possibly threading, given the name). The goal is to provide a modern, fast, and SEO-friendly website for the brand.

## Tech Stack
- **Framework:** Astro (v6.0+)
- **UI Library:** React (v19.0+)
- **Language:** TypeScript
- **Integrations:** `@astrojs/sitemap`, `@astrojs/react`
- **Styling:** Vanilla CSS (scoped within Astro components)
- **Runtime:** Node.js (>=22.12.0)

## Project Conventions

### Code Style
- **Astro Components:** Prefer `.astro` files for static UI and layouts.
- **React Components:** Use `.tsx` for interactive components. Place them in `src/components/`.
- **Styling:** Use scoped `<style>` tags within Astro components. For React, use CSS modules or standard CSS files imported into the component. Follow the Antigravity rule: prefer `clsx` over `class:list` for conditional classes.
- **Naming:** Use PascalCase for components and layouts (e.g., `Welcome.astro`, `Layout.astro`, `Counter.tsx`). Use kebab-case for assets and pages (e.g., `background.svg`, `index.astro`).

### Architecture Patterns
- **Directory Structure:**
  - `src/components/`: Reusable UI components.
  - `src/layouts/`: Base page templates.
  - `src/pages/`: Route-specific components (file-based routing).
  - `src/assets/`: Static assets like images and global styles.
- **Layouts:** Wrap pages in a common `Layout.astro` component to ensure consistency.

### Testing Strategy
[To be defined - no testing framework currently identified in package.json]

### Git Workflow
- **Branching Strategy:** Standard feature branching (assumed).
- **Commit Conventions:** Follow Conventional Commits format (feat, fix, chore, etc.).

## Domain Context
- **Industry:** Beauty/Personal Care (Hair Removal).
- **Target Audience:** Customers looking for threading or hair removal services.

## Important Constraints
- **Performance:** Maintain high performance and SEO scores, leveraging Astro's static site generation (SSG) capabilities.

## External Dependencies
- **Sitemap:** Automatically generated via `@astrojs/sitemap`.
