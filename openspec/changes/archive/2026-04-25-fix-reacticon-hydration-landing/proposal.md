# Fix ReactIcon Hydration in Landing Pages

## Motivation
The `ReactIcon` component uses a React `useEffect` to dynamically load icons on the client side. In the landing pages (specifically `landing/src/pages/booking/[id].astro`), this component is rendered without any Astro client directive (like `client:load`). As a result, the component does not hydrate on the client side, the `useEffect` is never triggered, and the icons remain in their fallback state (empty `<span>`).

## Proposed Solution
Add the `client:load` directive to all instances of the `ReactIcon` component within `.astro` files in the `landing` service where it is missing, ensuring that the components hydrate properly and the icons load.