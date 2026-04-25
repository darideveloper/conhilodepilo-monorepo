# admin-ui Specification Delta

## MODIFIED Requirements

### Requirement: Styled Markdown Preview
The Markdown editor preview SHALL have distinct typography styles that ADAPT to the project's brand colors and theme.

#### Scenario: Verify Dynamic Branding
- **Given** the `brand_color` in `CompanyProfile` is set to a specific color (e.g., Green).
- **When** viewing the Markdown preview.
- **Then** links and primary accents in the preview MUST use the derived primary shades (e.g., Green shades from `--brand-primary-600`).
- **And** borders and backgrounds MUST match the Unfold theme's base color palette.
