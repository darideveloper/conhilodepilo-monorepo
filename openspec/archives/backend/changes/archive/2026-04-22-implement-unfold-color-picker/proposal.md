# Proposal: Implement Unfold Color Picker for Company Brand Color

## Why
The current `brand_color` field in the `CompanyProfile` model is a plain `CharField`. Users must manually enter HEX or OKLCH strings, which is prone to error and provides a poor user experience. Since the project uses Django Unfold, we should leverage its built-in color picker widget to provide a visual interface for selecting the brand color.

## What Changes
- **Admin**: Update `CompanyProfileAdmin` to use `UnfoldAdminColorInputWidget` exclusively for the `brand_color` field.
- **Model**: Update `CompanyProfile` default `brand_color` to a HEX value for better picker initialization.
- **Verification**: Use Playwright and internal scripts to verify the widget and color math.

## Proposed Solution
- Update `CompanyProfileAdmin` to use the `UnfoldAdminColorInputWidget` for the `brand_color` field.
- Ensure the field continues to support existing color math logic (which derives the full Tailwind-like palette).
- Maintain compatibility with the current `RegexValidator` while favoring HEX for the visual picker.
- Explicitly verify and ensure all environment dependencies (specifically `django-unfold`) are correctly configured to support this widget.

## Scope
- **Admin UI**: Modify `booking/admin.py` to override the widget for `brand_color`.
- **Validation**: Ensure the picker's output (HEX) is correctly handled by existing validators and utility functions.
- **Dependencies**: While `django-unfold` is already installed, we will ensure it is correctly utilized. No additional third-party color picker libraries are required as Unfold's native solution is preferred for UI consistency.

## Impact
- **Improved UX**: Admins can visually select colors instead of typing codes.
- **Consistency**: The color picker matches the Unfold theme aesthetics.
- **System Integrity**: The derived color palette (`get_brand_config`) will continue to function correctly as it already supports HEX inputs. We will perform a regression check on the "color math" to ensure shades remain visually pleasing when derived from HEX.
- **Verification Rigor**: We will use Playwright to automate the verification of the color picker in the admin interface, using the development admin user (`admin` / `admin`).
- **State Management**: After verification, the `brand_color` will be restored to its original value (`#ee5837`) to maintain the project's current aesthetic.
