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

### Requirement: Spanish Admin Translations
The Django admin dashboard SHALL correctly display all booking-related field names, labels, and choice descriptions in Spanish.

#### Scenario: Verification of Booking Edit Page
- **WHEN** the administrator views the change page for a booking reservation
- **THEN** the labels for "Booking Services", "Is gift", "Buyer name", "Buyer email", "Recipient name", "Recipient email", "Pricing", "Original amount", "Discount amount", "Total amount", "Google sync status", "Success", "Google sync error", and "Last synced at" are displayed in Spanish.


