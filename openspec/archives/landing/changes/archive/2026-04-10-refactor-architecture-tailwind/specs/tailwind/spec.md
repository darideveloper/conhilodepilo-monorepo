## ADDED Requirements
### Requirement: Enforce Tailwind CSS exclusively over Vanilla
The project MUST heavily prioritize Tailwind CSS class utilities over bespoke `<style>` CSS in any given file, ensuring all design implementation passes through the Tailwind compiler.

#### Scenario: Writing new UI elements
- **WHEN** building or refactoring UI components
- **THEN** use inline Tailwind utility classes instead of writing custom CSS rules in a scoped `<style>` block.
- AND standard vanilla CSS is only allowed if it cannot be achieved via standard tailwind configuration or arbitrary values.
