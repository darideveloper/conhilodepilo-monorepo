# Design: Services UI Refactor

## Context
The API returns a nested data structure: Categories contain images and descriptions, while their child Services contain pricing and durations. 

## Architecture Decisions

### 1. New Component (`CategoryCard.tsx`)
Instead of forcing the existing `ServiceCard` to handle complex nested state, we will build a dedicated `CategoryCard`.
- **State Management:** It will use `useState` to track the `selectedService` (defaulting to the first service or `null`).
- **Interactive Elements:** Nested services will be rendered as a list of selectable pills/buttons within the card.
- **Dynamic Display:** Clicking a service pill will dynamically update a dedicated section within the card to show that specific service's price and duration.

### 2. Layout Shift (`CategoryShowcase.tsx`)
Because the top-level data now consists of Categories (likely only 3 to 4 items) rather than dozens of individual services, a slider (`ServicesSlider.tsx`) is no longer the best UX. We will replace it with a responsive CSS Grid (`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`). 

### 3. Styling & Branding
The new components will strictly adhere to the existing brand guidelines (using `brand-primary`, `brand-secondary`, `clsx` for conditional classes, and existing badge/button aesthetics).
