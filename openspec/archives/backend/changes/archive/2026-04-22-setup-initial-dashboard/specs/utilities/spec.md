# Capability: Utilities and Helpers

## ADDED Requirements

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
