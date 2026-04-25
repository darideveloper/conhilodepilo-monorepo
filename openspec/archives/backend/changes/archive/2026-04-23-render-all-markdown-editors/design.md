# Design: Global Markdown Editor Application

## Architecture Overview
The project uses `django-unfold` as its admin theme. Custom JavaScript is injected via `project/templates/admin/base_site.html` (which extends Unfold's base template). The script `static/js/load_markdown.js` is responsible for finding `textarea` elements and initializing SimpleMDE.

## Implementation Details
The current implementation uses a blacklist strategy:
```javascript
const noMarkdownIds = ["google_maps_src", "description"]
const notSelector = noMarkdownIds.map(id => `:not(#id_${id})`).join("")
textAreasSelector = `div > textarea${notSelector}`
```

We will transition to a whitelist-by-default strategy by removing the exclusions. The new logic will simply target all `div > textarea` elements. This selector is specific enough to target text areas within the Unfold admin form structure while avoiding potential collisions with other UI elements if they were to exist outside of form containers.

## Trade-offs
- **Potential Bloat**: If a field truly shouldn't be Markdown (e.g., a raw JSON field or a legacy field), it will now have an editor. However, in the current project context, all `TextField`s identified (mostly `description`) are intended for formatted content.
- **Safety**: By removing `google_maps_src`, we must ensure it doesn't break any specialized map-related text areas. If `google_maps_src` is a field that expects specific raw format, we should verify if it's still in use. (Research: `google_maps_src` is not present in `booking/models.py`, it might be a remnant or from another app not yet analyzed).

## Verification Plan
1.  **Manual Check**: Navigate to `EventType` and `Event` admin pages and verify that the `description` fields now show the SimpleMDE toolbar.
2.  **Regression Check**: Ensure that standard `CharField` inputs (regular text inputs) are NOT affected.
