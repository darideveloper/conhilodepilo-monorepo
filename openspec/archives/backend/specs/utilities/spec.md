# utilities Specification

## Purpose
TBD - created by archiving change setup-initial-dashboard. Update Purpose after archive.
## Requirements
### Requirement: Admin Permission Helpers
The project SHALL include utility functions to validate if a user belongs to administrative or support groups.

#### Scenario: Verify Admin Permissions
- Given a user who is a member of the "admins" group.
- When `is_user_admin(user)` is called.
- Then it returns `True`.

### Requirement: Selenium Automation Helpers
The project SHALL include helper functions to simplify the selection of web elements using Selenium.

#### Scenario: Select Selenium Elements
- Given a Selenium driver and a dictionary of selectors.
- When `get_selenium_elems` is called.
- Then it returns a dictionary mapping keys to their corresponding WebElements.

### Requirement: Media and Image Utilities
The project SHALL include utilities for resolving media URLs (handling both local and S3-based storage) and generating test images.

#### Scenario: Resolve Media URL
- Given a media object with a URL.
- When `get_media_url` is called.
- Then it returns the absolute URL including the configured host for local files, or the direct S3 URL.

### Requirement: Dynamic Branding Callbacks
The project SHALL include callback functions to resolve site title, header, and icon from the current company profile.

#### Scenario: Resolve Dynamic Header
- GIVEN a `CompanyProfile` with name "Custom Brand"
- WHEN `site_header_callback(request)` is called
- THEN it returns "Custom Brand".

### Requirement: Brand Color Derivation
The project SHALL include a utility to derive a full 11-step palette (50-950) from a base primary color.

#### Scenario: Exact Color Matching
- GIVEN a base color `#ee5837`
- WHEN `get_brand_config()` is called
- THEN the returned dictionary MUST map the exact base color to the `500` and `600` shades.

#### Scenario: Derive OKLCH Shades
- GIVEN a base color `oklch(0.68 0.28 296)`
- WHEN `get_brand_config()` is called
- THEN it returns a dictionary with adjusted luminance values for the remaining shades (e.g., 50, 400, 900).

