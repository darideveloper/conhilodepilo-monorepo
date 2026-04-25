# Layout Specification

## Purpose
Define the global HTML structure and common components that wrap all pages in the project.

## Requirements

### Requirement: Global Page Structure
Every page in the project MUST follow a consistent semantic structure provided by the primary layout.

#### Scenario: Structural Sequence
- **WHEN** a page is rendered using the `Layout.astro` component
- **THEN** it MUST contain exactly one `<header>` (via `Header.astro`).
- **AND** it MUST contain exactly one `<main>` element wrapping the page content.
- **AND** it MUST contain exactly one `<footer>` (via `Footer.astro`) as a sibling to `<main>`.

### Requirement: Centralized Main Wrapper
Individual pages MUST NOT provide their own `<main>` tag if they are wrapped by `Layout.astro`.

#### Scenario: Redundant Main Removal
- **GIVEN** an Astro page component using `Layout.astro`
- **WHEN** the page defines its content
- **THEN** it MUST NOT wrap its top-level content in a `<main>` tag, as the layout already provides it.

### Requirement: Persistent Footer
The global footer MUST be present on all pages that utilize the standard project layout.

#### Scenario: Automatic Footer Inclusion
- **GIVEN** a new page component
- **WHEN** it imports and uses `Layout.astro`
- **THEN** the `Footer.astro` component MUST be automatically rendered at the bottom of the page.
