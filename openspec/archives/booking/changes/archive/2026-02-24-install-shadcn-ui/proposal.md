# Proposal: Install and Setup shadcn/ui

This proposal outlines the installation and configuration of **shadcn/ui** using the latest version compatible with **Astro 5** and **Tailwind CSS v4**.

## Why
The project requires a robust and customizable component library to build a professional UI. Shadcn/ui provides a collection of re-usable components that follow best practices for accessibility and design, and it is fully compatible with the current tech stack (Astro, React, Tailwind v4).

## What Changes
- Install `shadcn` CLI and required dependencies (`lucide-react`, `clsx`, `tailwind-merge`, `tailwindcss-animate`).
- Configure `tsconfig.json` with `@/*` path aliases.
- Initialize `components.json` for shadcn/ui management.
- Update `src/styles/global.css` to align shadcn/ui CSS variables with the **GranadaGo** brand identity (Colors: Pomegranate Red, Cream, Charcoal).
- Implement `src/lib/utils.ts` for class merging.

## Goals
- Fully functional shadcn/ui setup in the project.
- Branding consistency between shadcn/ui components and the GranadaGo design analysis.
- Modern developer experience with path aliases.

## Scope
- Configuration files: `tsconfig.json`, `components.json`.
- Styling: `src/styles/global.css`.
- Utility functions: `src/lib/utils.ts`.
- Dependency management: `package.json`.

## Success Criteria
- `npx shadcn@latest add button` succeeds.
- A Button component can be imported using `@/components/ui/button`.
- The Button primary style matches the brand's Pomegranate Red (`#A62C2B`).
- `openspec validate` passes.
