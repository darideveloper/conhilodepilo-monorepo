# Design: Unfold Color Picker Integration

## Overview
The goal is to replace the standard text input for `brand_color` in the Django Admin with a visual color picker provided by `django-unfold`.

## Technical Details

### Widget Selection
We will use `unfold.widgets.UnfoldAdminColorInputWidget`. This widget renders an `<input type="color">` styled to match the Unfold dashboard. It natively outputs HEX color codes.

### Color Format & Compatibility
1. **Input/Output**: The picker will output HEX (e.g., `#682896`).
2. **Current Model**: The `CompanyProfile.brand_color` field uses a `RegexValidator` that allows both HEX and OKLCH.
   - HEX: `#[0-9a-fA-F]{6}`
   - OKLCH: `oklch\([\d.]+%? [\d.]+ [\d.]+\)`
3. **Color Math**: The `get_brand_config` function in `utils/callbacks.py` already handles both formats. If it receives a HEX color, it converts it to an approximation of OKLCH to generate the 50-950 shades.

### Implementation Pattern
The widget is applied in `booking/admin.py` using the `formfield_for_dbfield` method in `CompanyProfileAdmin`. This allows for surgical targeting of the `brand_color` field without affecting other `CharField` inputs like "Name" or "Currency".

```python
from unfold.widgets import UnfoldAdminColorInputWidget

class CompanyProfileAdmin(...):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "brand_color":
            kwargs["widget"] = UnfoldAdminColorInputWidget
        return super().formfield_for_dbfield(db_field, **kwargs)
```

## Testing Strategy

### Automated Verification (Playwright)
We will use Playwright to automate the verification of the color picker. The script will perform the following:
1.  **Authentication**: Log in to the admin panel using the predefined development credentials (`admin` / `admin`).
2.  **Navigation**: Go to the `CompanyProfile` change view.
3.  **Element Inspection**: Verify that the `brand_color` input element is present and has `type="color"`.
4.  **Interaction**: Programmatically change the color value and save the form.
5.  **Success Check**: Verify that the success message is displayed and the new color is saved in the database.

### State Restoration
To ensure no permanent changes to the project's visual identity during development/testing, the test script or a post-deployment task will restore the `brand_color` to its original value of `#ee5837`.
