# Proposal: Customize Unfold Branding

## Goal
Implement dynamic branding (colors, company name, and logo) for the Django Unfold admin interface using the `CompanyProfile` model. This allows the dashboard's appearance to be updated directly from the admin UI without code changes.

## Scope
- **Models**: Update `CompanyProfile` to include a `name` field and enhance `brand_color` validation.
- **Utilities**: Implement callbacks for Unfold dynamic settings and a color derivation helper for generating a full 11-step CSS variable palette (50-950) that respects exact user color matching for primary buttons.
- **Core Settings**: Register a new `branding` context processor.
- **Admin UI**: Configure Unfold to use callbacks and CSS variables; override the skeleton template to inject dynamic styles.

## Relationships
- Modifies `openspec/specs/booking-models/spec.md` to add branding fields.
- Modifies `openspec/specs/utilities/spec.md` to add branding callbacks.
- Modifies `openspec/specs/core-settings/spec.md` to add the context processor requirement.
- Modifies `openspec/specs/admin-ui/spec.md` to update the Unfold configuration and template requirements.
