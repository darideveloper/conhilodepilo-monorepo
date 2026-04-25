# Design: Cleanup Administrative Consistency

## 1. Global Context Processor Update
The `brand_theme_context` will be expanded to include dynamic site identity metadata.

```python
def brand_theme_context(request):
    from utils.callbacks import get_brand_config, site_title_callback, site_header_callback
    return {
        "brand_colors": get_brand_config(),
        "site_title": site_title_callback(request),
        "site_header": site_header_callback(request),
    }
```

## 2. Standardized Translation IDs
Following Django best practices, all translatable strings in the source code will use English as the source language (`msgid`).

**Mappings for `settings.py`:**
- `_("Gestión")` -> `_("Management")`
- `_("Reservas")` -> `_("Bookings")`
- `_("Servicios")` -> `_("Services")`
- `_("Configuración")` -> `_("Configuration")`
- `_("Perfil de Empresa")` -> `_("Company Profile")`
- `_("Autenticación")` -> `_("Authentication")`
- `_("Usuarios")` -> `_("Users")`
- `_("Grupos")` -> `_("Groups")`
- `"Dashboard"` -> `_("Dashboard")`

## 3. Localization Strategy
The `locale/es/LC_MESSAGES/django.po` file will be manually updated to map these new English `msgid`s to their Spanish counterparts. This is preferred over `makemessages` for this surgical cleanup to ensure we don't accidentally wipe out or fuzzy-match existing complex translations.

### Target Translation Table
| English (msgid) | Spanish (msgstr) |
| :--- | :--- |
| Management | Gestión |
| Bookings | Reservas |
| Services | Servicios |
| Configuration | Configuración |
| Company Profile | Perfil de Empresa |
| Authentication | Autenticación |
| Users | Usuarios |
| Groups | Grupos |
| Dashboard | Panel de Control |
| General | General |
| Global Availability | Disponibilidad Global |
| Business Hours | Horario Comercial |
| Holidays | Festivos |
| Client Information | Información del Cliente |
| Scheduling | Programación |
| Integrations | Integraciones |
| Manage | Gestionar |
| Actions | Acciones |
| Client | Cliente |
| Date/Time | Fecha/Hora |
| Status | Estado |
