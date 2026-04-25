# Project Context

## Purpose
A professional website for **Granada Go Tours**, offering high-quality guided tours in Granada, Spain. The tours are led by Alejandro, an official guide and historian, focusing on deep cultural immersion and historical accuracy. The site serves as a catalog for various tours (Monumental, Religious, Neighborhoods) and provides contact information for bookings.

## Tech Stack
- **Framework:** [Astro 5](https://astro.build/) (v5.17.1)
- **Styling:** [Tailwind CSS v4](https://tailwindcss.com/) (using `@tailwindcss/vite`)
- **Language:** [TypeScript](https://www.typescriptlang.org/) (Strict mode)
- **Utilities:** `clsx` (preferred for conditional and complex class management)
- **Data Source:** Guided tours are managed via `public/services.json`.

## Project Conventions

### Code Style
- **Conditional Classes:** Always use the `clsx` library for handling complex or conditional classes. Avoid Astro's native `class:list`.
- **TypeScript:** Adhere to strict TypeScript configurations as defined in `tsconfig.json`.
- **Formatting:** Standard Prettier/ESLint rules for Astro/TypeScript projects (if configured).

### Architecture Patterns
- **Component-Based:** Logic and UI are encapsulated in Astro components in `src/components`.
- **Static Site Generation (SSG):** Leveraging Astro's default SSG capabilities for performance and SEO.
- **Data-Driven:** Tour information is pulled from a centralized JSON file (`public/services.json`) to allow for easy updates to tour details.

### Testing Strategy
- [To be defined: No testing framework currently installed]

### Git Workflow
- Standard feature branching strategy.
- Clear, concise commit messages focusing on "why" rather than "what".

## Domain Context
- **Location:** Granada, Spain.
- **Key Sites:** Alhambra, Cathedral, Royal Chapel, Albaicín, Sacromonte, Cartuja, San Jerónimo.
- **Tour Focus:** Historical depth, official historian guides, private tours, cultural immersion (beyond conventional tourism).
- **Booking Flow:** Users browse tours and are directed to a contact form or WhatsApp for availability checks and booking.

## Important Constraints
- **Ticket Management:** Tours do not include monument tickets; customers must manage their own entries as noted in the tour disclaimers.
- **Language Standard:** Spanish is the primary language for this project. All user-visible text (labels, buttons, statuses, descriptions) MUST be in Spanish by default to ensure consistency for the core target audience in Granada, Spain. English may be supported as a secondary option in the future.

## External Dependencies
- **WhatsApp:** Direct link for bookings (`https://wa.me/...`).
- **Context7:** Primary source for up-to-date documentation and code examples during development.
