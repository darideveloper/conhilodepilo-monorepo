# brand-config Spec Delta

## MODIFIED Requirements

### Requirement: Visual Identity Tokens
The project SHALL have a consistent visual identity derived from a single brand color and supporting primary/secondary/accent tones.

#### Scenario: Define Unified Brand Color
- Given the primary Brand Red color: `oklch(0.577 0.245 27.325)`.
- When this is defined as the primary source for `--color-brand-red` and mapped to `--primary`.
- Then all primary UI elements MUST automatically inherit this color.

## ADDED Requirements

### Requirement: Theme Switching System
The system SHALL provide a mechanism for users to switch between Light and Dark themes.

#### Scenario: Toggle Theme
- Given a user viewing the application.
- When they interact with the theme toggle component.
- Then the application MUST flip between `.light` (default) and `.dark` mode instantly.

#### Scenario: Persist Theme Preference
- Given a user has selected a specific theme.
- When they revisit the site or reload the page.
- Then the application MUST load the saved theme from `localStorage` before rendering to avoid flashes.
