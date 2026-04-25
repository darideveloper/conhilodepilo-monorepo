# admin-ui Specification Delta

## MODIFIED Requirements

### Requirement: Markdown Support in Admin
Text areas in the admin interface SHALL support Markdown editing via SimpleMDE.

#### Scenario: Edit Markdown Field
- **Given** any model with a `TextField` (rendered as a `textarea`) in the Django admin.
- **When** the change form is rendered.
- **Then** the field MUST be enhanced with a SimpleMDE editor.
- **And** no `textarea` fields SHALL be excluded by default unless they are specifically tagged for raw editing.

#### Scenario: Description Fields as Markdown
- **Given** the `Event` or `EventType` models.
- **When** editing a record in the admin.
- **Then** the `description` field MUST display the SimpleMDE Markdown editor toolbar and preview.
