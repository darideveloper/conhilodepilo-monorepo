# Proposal: Refactor Data Fetching

## Goal
Transition the project from local, fixed/hardcoded data (JSON files for services and a JS array for courses) to a scalable API architecture. Data will be fetched via dedicated scripts located in `src/lib/api/` mimicking a real external API.

## Problem
Currently, the application data is tightly coupled to the codebase. Services are managed via Astro Content Collections (local JSON files in `src/content/services`), and courses are hardcoded directly inside `src/components/organisms/CoursesSection.astro`. This approach does not scale when content updates frequently or is managed externally (e.g., via a CMS or dashboard service).

## Scope
- Create `src/lib/api/` directory for separated API call scripts.
- Implement `getServices` and `getCourses` fetching dummy data.
- Refactor `ServicesSlider` and pages (`index.astro`, `design-system.astro`) to consume data from `getServices`.
- Refactor `CoursesSection` to consume data from `getCourses`.
- Update corresponding component interfaces and handle dynamic image URLs.
- Delete unused content collection configurations and local JSON files.

## Out of Scope
- Implementing a real dashboard database or CMS.
- Implementing authentication or authorization.
