# Proposal: Implement React Services Slider

## Goal
Create a scalable React component utilizing Swiper.js to handle 30+ service cards efficiently. The slider must include top filter buttons (based on service categories) and will initially be tested and isolated on the design system page.

## Context
Currently, the `ServicesGrid.astro` component displays a simple grid which is suitable for 4 cards, but does not scale for a production scenario containing 30+ service cards. Implementing a React-based slider with `swiper` will allow pagination and category filtering, ensuring the UI remains clean and manageable. The changes will be isolated as a new `ServicesSlider.tsx` component and tested on the `design-system.astro` page before affecting the landing page.

## Proposed Changes
1. Create a `ServiceCard.tsx` React component mirroring the design of `ServiceCard.astro`.
2. Create a `ServicesSlider.tsx` React component.
3. Implement category filtering buttons above the slider.
4. Integrate Swiper.js to display the filtered service cards.
5. Add the component to `design-system.astro` to test and validate visually.