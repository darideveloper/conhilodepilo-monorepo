# Proposal: Install and setup Tailwind CSS v4

Install and configure Tailwind CSS v4 using the official Astro integration and Vite plugin as per the Astro documentation.

## Goals

- Install Tailwind CSS v4 dependencies.
- Configure Tailwind CSS v4 in the Astro project.
- Set up a global stylesheet for Tailwind imports.
- Ensure Tailwind is available across the project.

## User Review Required

> [!IMPORTANT]
> This proposal uses the `@tailwindcss/vite` plugin which is the standard for Tailwind v4 in Astro.

## Proposed Changes

### Configuration

- Run `npx astro add tailwind` to install and configure the integration.
- Create or update `src/styles/global.css` to include `@import "tailwindcss";`.
- Import `src/styles/global.css` in `src/layouts/Layout.astro`.

### Styles

- Tailwind classes will be available in all Astro and React components.
