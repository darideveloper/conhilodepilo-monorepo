# core-settings Spec Delta: Cleanup Administrative Consistency

## MODIFIED Requirements

### Requirement: Default Language Configuration
The project's default language SHALL be configured to Spanish (`es`), and it SHALL support local translation overrides using English as the source language for all translatable strings.

#### Scenario: Standardized Localization Identifiers
- **Given** any ModelAdmin, context processor, or settings file.
- **When** defining translatable strings using `_()`.
- **Then** the string inside `_()` MUST be in English.
- **And** the Spanish translation MUST be provided in the corresponding `.po` file.

#### Scenario: Comprehensive UI Localization
- **Given** the Spanish locale is active.
- **When** navigating the admin sidebar, tabs, and fieldsets.
- **Then** all labels MUST appear in Spanish.
- **And** no English fallback labels SHOULD be visible in the primary navigation or configuration areas.

### Requirement: Branding Context Processor
The project SHALL include a context processor to provide derived brand colors and site identity to all templates.

#### Scenario: Inject Site Identity Globally
- **Given** the `brand_theme_context` context processor is registered.
- **When** any template is rendered.
- **Then** the context variables `site_title` and `site_header` MUST be available and populated from the `CompanyProfile` model via callbacks.
