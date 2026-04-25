# Design: Fix Service Card Hover Zoom

## Problem
The `ServicesSlider` component wraps the Swiper slider in a `div` with the Tailwind `group` class. The `ServiceCard` component (both React and Astro versions) also uses the `group` class on its root element and `group-hover:scale-105` on its image.

In Tailwind CSS, `group-hover` triggers if **any** parent element has the `group` class. Because the slider container is a parent to all cards, hovering anywhere over the slider (including between cards) activates the zoom effect for all cards at once.

## Solution
We will implement **Tailwind Labeled Groups** to isolate the hover state. By labeling the card's group, we ensure its internal hover effects only respond to the card itself being hovered.

### Technical Implementation
1.  **Label the Card Group**: Change the `group` class on the `ServiceCard` and `CourseCard` root elements to `group/card`.
2.  **Target the Labeled Group**: Change the `group-hover:scale-105` utility on the images to `group-hover/card:scale-105`.

This approach is superior to removing the `group` class from the `ServicesSlider`, as that parent group might be intended for other UI behaviors (like showing navigation buttons on hover).

## Impact
- **ServiceCard (React & Astro)**: Updated to use labeled groups.
- **CourseCard (Astro)**: Updated to use labeled groups for consistency.
- **User Experience**: Zoom effect becomes surgical and card-specific.
- **Maintainability**: Prevents future parent `group` usage from accidentally triggering card hover effects.
