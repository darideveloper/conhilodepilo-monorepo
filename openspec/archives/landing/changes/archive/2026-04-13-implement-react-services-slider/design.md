# Design: React Services Slider

## Architecture & Technical Decisions
- **Framework:** React is chosen to handle the complex state of category filtering and slider initialization.
- **Slider Library:** `swiper` (already in `package.json`) will be used.
- **Component Isolation:** The new `ServicesSlider.tsx` will be completely independent of the existing `ServicesGrid.astro` to ensure no regressions occur on the live landing page.
- **Props & State:** The component will accept an array of service objects. It will maintain an active category state and filter the services dynamically before passing them to Swiper.
- **Card Reuse:** We need a React version of the `ServiceCard` to map the raw service data cleanly inside Swiper slides, since we cannot easily render Astro components inside a React client component. We will create a `ServiceCard.tsx` to mirror the Astro component visually.

## Trade-offs
- Duplicating the `ServiceCard` logic in React adds a slight maintenance overhead, but it is necessary since Astro components cannot be interpolated inside React client components that change state dynamically on the client.