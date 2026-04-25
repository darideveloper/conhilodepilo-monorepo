# Design: Refactor Layout Structure

## Architectural Overview
The project currently delegates the responsibility of the main content wrapper (`<main>`) and the global footer to individual pages. This proposal shifts that responsibility to the `Layout.astro` component, which is the root wrapper for all pages.

### Proposed Structure
```astro
<!-- src/layouts/Layout.astro -->
<Header />
<main class={className}>
    <slot />
</main>
<Footer />
```

## Considerations

### 1. Semantic Integrity
The `<main>` element should represent the dominant content of the `<body>`. By placing it in the layout, we guarantee its presence on every page, which is beneficial for accessibility (ARIA `role="main"`).

### 2. Layout Flexibility
The `Layout` component already accepts a `class` prop. We will apply this class to the `<main>` tag instead of the `<body>` (or keep it on the body if it controls global background/font, and perhaps add a new prop for the main container if needed). 

In the current `Layout.astro`:
```astro
<body class={clsx("min-h-full font-sans bg-ui-bg-light text-ui-text-main antialiased selection:bg-brand-primary/30", className)}>
    <Header />
    <slot />
</body>
```
If we move `className` to `<main>`, we need to ensure that specific page paddings (like `py-20` in `design-system.astro`) are preserved.

### 3. Footer Integration
The `<Footer />` component is an organism that should be present on all user-facing pages. Moving it to the layout ensures it's never forgotten when creating new pages.

## Implementation Strategy
1. Update `Layout.astro` to include `<main>` and `<Footer />`.
2. Refactor `index.astro` to remove its own `<main>` and `<Footer />`.
3. Refactor `design-system.astro` to remove its own `<main>`.
4. Ensure the `className` prop in `Layout.astro` is handled correctly so pages can still apply specific styles to the main container.
