# Design: Add Image to EventType

## Problem
Administrators cannot currently associate images with event types, limiting the visual richness of the service catalog.

## Solution
Add a `models.ImageField` to the `EventType` model.

### Model Changes
- **Field name:** `image`
- **Type:** `models.ImageField`
- **Parameters:**
  - `verbose_name`: Translatable label (e.g., `_("Image")`).
  - `upload_to`: Set to `"event_types/"`.
  - `null=True`, `blank=True`: Make it optional.

### Admin Changes
- Add the `image` field to the `fieldsets` in `EventTypeAdmin`.

### Storage
The project seems to be using standard Django media storage (based on the presence of a `media/` directory and `storage_dashboards.py`).

## Trade-offs
- **Complexity:** Low. Standard Django model field addition.
- **Dependencies:** Requires `Pillow` (already likely present if `CompanyProfile` has a `logo` field).
