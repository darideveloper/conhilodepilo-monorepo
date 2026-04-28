# Proposal: Fix Header Navigation Links

## Why
In the Landing project, the main navigation links in the Header component currently use relative hash links (e.g., `#servicios`). This works correctly when the user is on the homepage. However, if the user navigates to a subpage (e.g., an individual service page), clicking the header links will fail to navigate to the correct section because the links lack the root path (`/`).

## What Changes
Update the navigation links in the `landing/src/components/organisms/Header.astro` component to use absolute paths to the homepage sections (e.g., `/#servicios`). This ensures that the navigation works properly regardless of the current page the user is viewing.

- **Navigation:** Header links will accurately navigate to the homepage sections from any route in the application.
- **Codebase:** A minor change to the `navLinks` array in the `Header.astro` component.