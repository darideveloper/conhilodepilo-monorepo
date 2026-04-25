# Project Context

## Purpose
The `conhilorepilo` ecosystem is a multi-service platform consisting of a Django-based management dashboard, a Granada cultural tourism site (Granada Go Tours), and a beauty services site (Con Hilo Depilo). 

## Shared Architecture
- **Backend:** Python/Django (Dashboard & API)
- **Frontend:** Astro (SSG/SSR) with React integration
- **Versioning/CI:** Monorepo architecture managed via centralized documentation.

## Global Conventions

### Git Workflow
- **Commit Format:** Strictly follows [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): subject`.
- **Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.

### Documentation (OpenSpec)
- **Global:** Cross-service architecture, API contracts, and global dependencies are defined in `openspec/`.
- **Local:** Implementation-level details for each service remain in their respective `/openspec` folders.

---

# Service: Backend (Dashboard)

## Purpose
A modern Django-based dashboard and administration system to manage content for the ecosystem.

## Tech Stack
- **Framework:** Python 3.12, Django 5.2+
- **API:** Django REST Framework (DRF)
- **Admin UI:** Django Unfold (Tailwind-based)
- **Database:** PostgreSQL (production), SQLite (testing)

## Service-Specific Conventions
- **Configuration:** Strictly environment-variable-first (`python-dotenv`).
- **API Standards:** Centralized error handling (`project/handlers.py`) and metadata-rich pagination (`project/pagination.py`).
- **Synchronization:** API endpoint changes MUST be accompanied by updates to automated tests and Bruno OpenCollection files (`bruno/**/*.yml`).

---

# Service: Landing (Granada Go Tours)

## Purpose
A catalog for guided cultural tours in Granada, Spain.

## Tech Stack
- **Framework:** Astro 5, Tailwind CSS v4, TypeScript
- **Data:** `public/services.json`

## Service-Specific Conventions
- **Language:** Primary language is Spanish (default).
- **Styling:** Preference for `clsx` for conditional classes (no `class:list`).

---

# Service: Booking (Con Hilo Depilo)

## Purpose
A modern, fast, SEO-friendly website for a beauty/hair removal service.

## Tech Stack
- **Framework:** Astro 6, React 19, TypeScript

## Service-Specific Conventions
- **Component Strategy:** `.astro` for static UI, `.tsx` for interactive components.
- **Styling:** Scoped `<style>` tags for Astro; CSS modules/standard CSS for React. Preference for `clsx`.
