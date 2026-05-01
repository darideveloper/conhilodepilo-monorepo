# i18n-admin Specification

## Purpose
This specification defines the requirements for the internationalization (i18n) of the Django admin interface, ensuring that all administrative views, fields, and labels are correctly translated into Spanish.
## Requirements
### Requirement: Admin Interface Internationalization
The Django admin interface MUST be fully translated into Spanish to provide a localized experience for administrators.

#### Scenario: Displaying Spanish Labels in Admin
- **Given** the application language is set to Spanish (`es`).
- **When** an administrator accesses any model list or change view.
- **Then** all field names (e.g., "Nombre", "Fecha de inicio"), model names (e.g., "Reservas", "Perfil de Empresa"), and section headers (e.g., "Configuración de UI") MUST be displayed in Spanish.

### Requirement: Translation File Completeness
The Spanish translation catalog (`django.po`) MUST contain valid translations for all strings wrapped in translation functions within the dashboard codebase.

#### Scenario: Compiling Translations
- **Given** the updated `django.po` file.
- **When** running the `compilemessages` command.
- **Then** the command MUST succeed and generate a `django.mo` file containing all defined translations.

