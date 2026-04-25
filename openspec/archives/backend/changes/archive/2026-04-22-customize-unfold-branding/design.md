# Design: Dynamic Unfold Branding

## Architecture
The dynamic branding system decouples the admin interface appearance from static settings by using per-request callbacks and CSS variable injection.

### 1. Source of Truth
The `CompanyProfile` model (a Singleton) stores the user-defined branding assets:
- `name`: Displayed as the site title and header.
- `logo`: Used in the sidebar and login screen.
- `brand_color`: The base primary color (supports HEX and OKLCH).

### 2. Dynamic Resolution
Unfold supports passing function paths (strings) to its configuration keys. We implement:
- `site_title_callback`: Resolves the company name.
- `site_header_callback`: Resolves the company name for the main header.
- `site_icon_callback`: Resolves the logo URL.

### 3. Color Math & CSS Variables
Tailwind (via Unfold) requires a full 11-step palette of a primary color (50 to 950).
- A utility function `get_brand_config` derives these shades from the base `brand_color`.
- It maps the user's exact `brand_color` directly to the `500` and `600` shades to ensure primary buttons match the exact configured color.
- For other shades, it performs "color math" (adjusting luminance/chroma) based on the OKLCH color space. If a HEX color is provided, it approximates the OKLCH values to generate a consistent palette.
- These 11 shades are passed to the templates via a context processor.

### 4. Template Injection
The default Unfold `skeleton.html` is overridden to include a `<style>` block in the `extrahead` block. This block maps the derived shades to CSS variables (e.g., `--brand-primary-500`) using the ID `unfold-custom-brand-colors` to avoid conflicts with Unfold's internal styles. The Unfold `COLORS` configuration is then updated to reference these variables.

## Trade-offs
- **Performance**: Each admin request performs a database lookup for the Singleton `CompanyProfile`. Given the low frequency of admin requests and the efficiency of Singleton lookups, this is acceptable. Caching could be added later if needed.
- **Color Validation**: To ensure the "color math" works, the `brand_color` field must be validated to ensure it follows a predictable format (HEX or OKLCH).
