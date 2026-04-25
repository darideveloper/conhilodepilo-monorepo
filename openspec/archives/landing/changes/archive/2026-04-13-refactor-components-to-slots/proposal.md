# Proposal: Refactor components to use slots for dynamic content

## Problem
Several components (`SectionHeader`, `ServiceCard`, `CourseCard`, `InfoCard`) currently use props for content like titles and descriptions. This limits flexibility when the content requires HTML formatting (e.g., bold text, icons, or custom links) without adding an excessive number of props.

## Proposed Solution
Refactor these components to use Astro slots for dynamic content areas. This allows developers to pass any HTML or other components directly into the content regions of a component, providing maximum flexibility while maintaining structural consistency.

## Benefits
- **Flexibility:** Supports rich text (bold, italic, etc.) and custom icons within content areas.
- **Maintainability:** Reduces the number of props needed for various content configurations.
- **Composability:** Allows components to be used as containers for more complex layouts.

## Constraints
- **Backwards Compatibility:** Maintain existing props as defaults when possible, or update all instances of the components in the codebase.
- **Atomic Design:** Ensure refactored components still adhere to the Atomic Design structure defined in the architecture spec.
