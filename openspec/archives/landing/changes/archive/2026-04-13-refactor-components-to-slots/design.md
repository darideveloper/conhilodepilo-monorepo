# Design: Component Slot Refactoring

## Strategy
We will transition from prop-based content to slot-based content for molecules and organisms that require flexible layout management.

### Patterns
For components that currently use a `title` prop:
- Use a named slot `<slot name="title" />` or a default slot if appropriate.
- Provide a default implementation using the existing `title` prop if it's still useful for simple text-only use cases.

For `SectionHeader`:
- Replace `title` prop usage with `<slot name="title">` fallback.
- Replace `subtitle` prop usage with `<slot name="subtitle">` fallback.

For `InfoCard`:
- It already has a `icon` slot.
- Refactor `text` prop to a default slot or a named `content` slot.

For `ServiceCard` & `CourseCard`:
- Refactor `description` to a slot to allow for rich text or additional icons.

## Architectural Impact
- **Molecules:** Become more generic "containers" for their respective content types.
- **Consistency:** All card-like components will follow a similar pattern for content injection.

## Trade-offs
- **Verbosity:** Using slots in the parent component can be slightly more verbose than passing a simple string prop.
- **Validation:** String props are easier to validate via TypeScript interfaces than slot content.
