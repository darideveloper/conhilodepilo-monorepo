# Proposal: Fix Markdown List Rendering

## Why
Currently, markdown content rendered in the application (like service descriptions and course details) is losing its bullet points and alignment because of overriding styles and insufficient padding, making the content hard to read and inconsistent with the design.

## What Changes
1.  **Introduce a `markdown` class:** Create a wrapper class in `global.css` that specifically targets markdown content to provide consistent list styling (`list-style: disc`), margins, and padding.
2.  **Define Global Markdown Styles:** Add scoped styles for `ul` and `li` inside `.markdown` to restore bullet points, add top/bottom margins to lists, and improve individual list item padding.
3.  **Update Rendering Components:** Apply the `.markdown` class globally to all containers wrapping parsed markdown content, including the booking page, `CourseCard.astro`, and `ServiceCard.astro`.
