# Tasks: Customize Unfold Branding

- [x] **Model Enhancement**
  - [x] Add `name` field to `CompanyProfile` model in `booking/models.py`.
  - [x] Add `RegexValidator` to `brand_color` field to support HEX and OKLCH.
  - [x] Create and apply migrations.
  - [x] **Validation**: Verify `CompanyProfile` can be saved with a custom name and a valid OKLCH color in the admin.

- [x] **Dynamic Callbacks**
  - [x] Implement `site_title_callback`, `site_header_callback`, and `site_icon_callback` in `utils/callbacks.py`.
  - [x] Implement `get_brand_config` in `utils/callbacks.py` to derive a full 11-step color palette (50-950), ensuring the exact base color maps to the 500 and 600 shades.
  - [x] **Validation**: Write a unit test to verify `get_brand_config` returns correct shades for a given OKLCH color.

- [x] **Context Processor**
  - [x] Create `project/context_processors.py` with the `branding` function.
  - [x] Register `project.context_processors.branding` in `TEMPLATES` in `project/settings.py`.
  - [x] **Validation**: Verify `brand_colors` is available in the template context via a simple view or the admin.

- [x] **Admin UI Configuration**
  - [x] Update `UNFOLD` settings in `project/settings.py` to use callback paths for `SITE_TITLE`, `SITE_HEADER`, and `SITE_ICON`. Comment out `SITE_LOGO` to ensure the brand name displays next to the logo.
  - [x] Update `UNFOLD["COLORS"]` to use `var(--brand-primary-XXX)` CSS variables for all 11 shades.
  - [x] **Validation**: Verify admin starts without errors and uses fallback colors if CSS variables are missing.

- [x] **Template Override**
  - [x] Create `project/templates/unfold/layouts/skeleton.html` extending the base Unfold skeleton.
  - [x] Add `<style id="unfold-custom-brand-colors">` block in the `extrahead` block to inject CSS variables.
  - [x] **Validation**: Inspect the admin dashboard in the browser to confirm CSS variables are present in the `:root` and applied to elements.
