# Proposal: SEO Implementation & Standardization

## Change ID
`seo-implementation`

## Summary
Standardize SEO practices for the project by implementing dynamic metadata, structured data, missing favicons/manifests, and performance optimizations as documented in `astro-seo.md`.

## Architectural Reasoning
To align with the project's SEO standards, we must transition from static layout headers to a dynamic, component-based SEO management system. This ensures better search visibility, consistent branding, and proper multi-language support (if added later).

## Scope
- Assets: Icons and manifest generation.
- Components: New `BaseSEO.astro` for dynamic metadata.
- Layout: Refactoring `Layout.astro` to use the new SEO system.
- Environment: Configuration for indexing control.
