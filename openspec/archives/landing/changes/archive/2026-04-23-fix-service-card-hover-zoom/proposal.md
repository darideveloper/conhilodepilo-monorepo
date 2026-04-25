# Proposal: Fix Service Card Hover Zoom

The goal of this change is to fix a UI bug in the `ServicesSlider` where hovering over the slider container causes all `ServiceCard` components to trigger their hover zoom effect simultaneously. It also applies the same fix to `CourseCard` for consistency and future-proofing.

## Change ID
`fix-service-card-hover-zoom`

## User Goal
Ensure that the zoom effect on service and course cards is isolated to the specific card being hovered, providing a predictable and polished user experience.

## Capabilities
- `isolated-card-hover`: Use Tailwind CSS labeled groups to isolate the hover state of the `ServiceCard` and `CourseCard` components from their parent containers.

## Related Changes
- `apply-design-system`: This change refines the hover behavior introduced during the design system implementation.

## Proposed Specs
- `specs/components/spec.md`
