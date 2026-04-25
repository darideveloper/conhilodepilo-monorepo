# Design: Multilingual Model Metadata

## Architectural Approach

The implementation will focus on the Django model and admin layers, leveraging `django.utils.translation.gettext_lazy` (aliased as `_`) to ensure that strings are translated at runtime based on the user's active language.

### 1. App Configuration
The `AppConfig` in `booking/apps.py` will be updated to include a translatable `verbose_name`. This ensures the app name appears correctly in the admin index.

### 2. Model Metadata
Each model in `booking/models.py` will have an explicit `Meta` class containing:
- `verbose_name`: The singular name of the model.
- `verbose_name_plural`: The plural name of the model.

### 3. Field Definitions
All model fields will be updated to include an explicit `verbose_name` as the first positional argument or as a keyword argument. This ensures that:
- Form labels in the admin are translatable.
- Column headers in list views are translatable.
- Error messages referencing fields are translatable.

### 4. Admin Customizations
Custom methods in `booking/admin.py` that provide labels (via `.short_description` or `.verbose_name`) will be verified to use translation hooks.

### 5. Translation Workflow
- **Extraction**: `python manage.py makemessages -l es -l en` will be used to update `.po` files.
- **Translation**: Spanish strings will be refined, and English strings will be added.
- **Compilation**: `python manage.py compilemessages` will generate the `.mo` files used by Django.

## Trade-offs
- **Verbosity**: Adding `verbose_name` to every field increases the code volume in `models.py`, but it is necessary for full control over translations.
- **Maintenance**: Every new field added in the future must also follow this pattern to maintain consistency.
