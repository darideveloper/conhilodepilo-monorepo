# admin-ui Specification Delta

## ADDED Requirements

### Requirement: Styled Markdown Preview
The Markdown editor preview SHALL have distinct typography styles to ensure content is easily readable and visually representative of the final rendered output.

#### Scenario: Verify Heading Styles
- **Given** a user is editing a Markdown field in the admin.
- **When** the user enters a heading (e.g., `# Heading 1`) and clicks the "Preview" button.
- **Then** the preview MUST render the heading with a larger font size and increased font weight compared to body text.

#### Scenario: Verify List Styles
- **Given** a user enters a bulleted list in the editor.
- **When** the "Preview" button is toggled.
- **Then** the list items MUST display visible markers (e.g., dots or numbers) and have appropriate left indentation.
- **And** the styles MUST NOT leak into the rest of the admin interface.
