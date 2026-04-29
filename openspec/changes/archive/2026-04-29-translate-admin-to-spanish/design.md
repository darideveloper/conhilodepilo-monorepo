# Design: Admin Interface Translation

## Workflow
The translation process follows standard Django internationalization practices:
1.  **Source Language**: English remains the primary source language in the code. This ensures compatibility with common development tools and allows for future translations into other languages (e.g., Portuguese, French) if needed.
2.  **Extraction**: `makemessages` is used to extract all strings wrapped in `_()` from the `.py` files.
3.  **Localization**: The extracted strings are translated into Spanish in `backend/locale/es/LC_MESSAGES/django.po`.
4.  **Compilation**: `compilemessages` converts the `.po` file into a binary `.mo` file used by Django at runtime.

## Key Decisions

### Source Strings vs. Direct Spanish in Code
We decided to keep English source strings instead of writing Spanish directly in the `verbose_name` and `default` attributes of the models.
- **Pros**: Maintains the infrastructure for multi-language support; cleaner codebase for developers who may be more used to English identifiers.
- **Cons**: Requires keeping the `.po` file in sync.

### Handling Hardcoded Defaults
Some fields in `CompanyProfile` (like `availability_free_label`) have hardcoded English defaults. These will be wrapped in `_()` so they can be translated via the catalog, while maintaining the English default in the database/schema level.

## Terminology Mapping & Exhaustive String List

To ensure consistency and full coverage, the following strings have been identified for translation:

### 1. App & Models
- **Booking Management** -> Gestión de Reservas
- **Company Profile** -> Perfil de Empresa
- **Event Type / Event Types** -> Tipo de Servicio / Tipos de Servicio
- **Service / Services** -> Servicio / Servicios
- **Company Availability / Company Availabilities** -> Disponibilidad General / Disponibilidades Generales
- **Company Weekday Slot / Company Weekday Slots** -> Horario Semanal / Horarios Semanales
- **Company Date Override / Company Date Overrides** -> Excepción de Fecha / Excepciones de Fecha
- **Service Availability / Service Availabilities** -> Disponibilidad de Servicio / Disponibilidades de Servicio
- **Service Weekday Slot / Service Weekday Slots** -> Horario Semanal de Servicio / Horarios Semanales de Servicio
- **Service Date Override / Service Date Overrides** -> Excepción de Servicio / Excepciones de Servicio
- **Booking / Bookings** -> Reserva / Reservas
- **Event Type Group / Event Type Groups** -> Agrupación de Servicios / Agrupaciones de Servicios

### 2. Fields & Labels
- **Start date / End date** -> Fecha de inicio / Fecha de fin
- **Start time / End time** -> Hora de inicio / Hora de fin
- **Weekday** -> Día de la semana
- **Date** -> Fecha
- **Is available** -> Está disponible
- **Available / Unavailable** -> Disponible / No disponible
- **Name / Description / Image / Price** -> Nombre / Descripción / Imagen / Precio
- **Duration (minutes)** -> Duración (minutos)
- **Booking cooldown (minutes)** -> Tiempo de espera entre reservas (minutos)
- **Brand color / Logo / Currency** -> Color de marca / Logo / Moneda
- **Contact email / Contact phone** -> Email de contacto / Teléfono de contacto
- **Payment model** -> Modelo de pago
- **Allow overlap** -> Permitir solapamiento
- **Client name / Client email / Client phone** -> Nombre del cliente / Email del cliente / Teléfono del cliente
- **Status** -> Estado
- **Special requests** -> Peticiones especiales
- **Google event ID / Stripe payment ID** -> ID de evento de Google / ID de pago de Stripe
- **Privacy policy URL** -> URL de política de privacidad

### 3. UI Labels (Configurable Defaults)
- **Service Category** -> Categoría de Servicio
- **Consultation** -> Consulta
- **Available** -> Disponible
- **Partial** -> Parcial
- **Fully Booked** -> Completo
- **Add-ons** -> Extras

### 4. Choices & Enums
- **Weekdays**: Monday -> Lunes, Tuesday -> Martes, etc.
- **Payment Models**: Pre-paid -> Prepago, Post-paid -> Pago posterior
- **Booking Status**: Pending -> Pendiente, Confirmed -> Confirmada, Paid -> Pagada, Cancelled -> Cancelada
- **Environments**: Production -> Producción, Staging -> Pruebas (Staging), Development -> Desarrollo, Local -> Local

### 5. Admin Interface (Fieldsets, Tabs, Buttons)
- **General / Contact Information / UI Labels** -> General / Información de Contacto / Etiquetas de UI
- **Client Information / Scheduling / Integrations** -> Información del Cliente / Programación / Integraciones
- **Scheduling Configuration** -> Configuración de Programación
- **Global Availability / Business Hours / Holidays** -> Disponibilidad Global / Horario Comercial / Festivos y Excepciones
- **Service Week Slots / Service Availability / Service Date Overrides** -> Horarios del Servicio / Disponibilidad / Excepciones
- **Client / Date/Time / Actions / Manage** -> Cliente / Fecha/Hora / Acciones / Gestionar
- **Dashboard / Management / Configuration / Authentication** -> Panel / Gestión / Configuración / Autenticación
- **Users / Groups** -> Usuarios / Grupos
- **Spanish / English** -> Español / Inglés

### 6. Messages & Validation
- **Start date cannot be after end date.** -> La fecha de inicio no puede ser posterior a la fecha de fin.
- **Start time must be before end time.** -> La hora de inicio debe ser anterior a la hora de fin.
- **Start and end times are required if available.** -> Las horas de inicio y fin son obligatorias si está disponible.
- **Enter a valid HEX color or OKLCH format...** -> Introduzca un color HEX válido o formato OKLCH...
