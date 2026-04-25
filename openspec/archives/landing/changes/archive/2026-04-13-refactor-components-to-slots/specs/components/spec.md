# components Specification

## Purpose
Define the requirements for UI components to ensure consistency, flexibility, and adherence to the design system.

## ADDED Requirements

### Requirement: Flexible Content via Slots
Molecules and Organisms that display content such as titles, subtitles, or descriptions MUST provide slots for these content areas to allow for dynamic and rich formatting.

#### Scenario: `SectionHeader` slots
- **GIVEN** a `SectionHeader` component
- **WHEN** passing a `title` as a prop
- **THEN** it renders the title in an `H2` tag
- **BUT WHEN** providing a `<slot name="title">`
- **THEN** it renders the slot content instead of the `title` prop

#### Scenario: `InfoCard` default slot
- **GIVEN** an `InfoCard` component
- **WHEN** providing children content
- **THEN** it renders that content as the card body text
- **AND** it MUST support a `text` prop as a fallback for simple text content

#### Scenario: `ServiceCard` and `CourseCard` slots
- **GIVEN** a `ServiceCard` or `CourseCard` component
- **WHEN** providing content in the default slot
- **THEN** it renders as the card's description
- **AND** it MUST support a `description` prop as a fallback
