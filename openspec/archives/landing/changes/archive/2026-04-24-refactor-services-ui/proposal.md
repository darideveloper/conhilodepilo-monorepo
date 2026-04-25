# Proposal: Refactor Services UI

## Goal
Overhaul the services UI to a "Category-first" design, creating new components that properly map to the nested `ServiceCategory` -> `Service` structure of the backend API, while maintaining the brand's visual identity.

## Problem
The current UI (`ServicesSlider` and `ServiceCard`) expects a flat array of services, each with its own image. However, the backend API structures data into Categories (which contain the image and main description) and nested Services (which lack images but contain specific price and duration details). Flattening this array resulted in empty images and lost category descriptions. Modifying the original `ServiceCard` to handle this nested state would bloat it and break backward compatibility.

## Scope
- Add `getServiceCategories` to `src/lib/api/getServices.ts` to return the unflattened array.
- Update `getServices` to propagate category images to individual services (fixes the Design System view).
- Create a new interactive React component `CategoryCard.tsx` that mirrors the visual style of `ServiceCard`.
- Create a new React layout component `CategoryShowcase.tsx` to replace the slider on the homepage.
- Integrate `CategoryShowcase` into `src/pages/index.astro`.
- Retain the original `ServiceCard` for backward compatibility in the `design-system.astro` page.

## Out of Scope
- Modifying the existing `ServiceCard` or `ServicesSlider` components (they will simply be swapped out on the homepage).
