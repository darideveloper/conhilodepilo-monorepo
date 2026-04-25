# Design: Event Admin Tab Refinement

## Tab Reordering and Renaming
The `EventAdmin.tabs` configuration will be updated in `booking/admin.py`. The new labels will use Django's `gettext_lazy` (`_()`) to facilitate translation.

| Current Label | New Label (English) | Spanish Translation | Related Inline/Fieldset |
|---------------|---------------------|---------------------|-------------------------|
| General | General | General | fieldsets |
| Business Hours | Service Week Slots | Franjas horarias de servicio | slots |
| Date Ranges | Service Availability | Disponibilidad de servicio | availabilities |
| Overrides | Service Date Overrides | Excepciones de fecha de servicio | overrides |
| Bookings | Booking | Reserva | bookings |

## Read-Only Booking Inline
To remove the "Agregar booking adicional" (Add Booking) button, we will override `has_add_permission` in `BookingInline`.

```python
class BookingInline(BaseTabularInline):
    # ...
    def has_add_permission(self, request, obj=None):
        return False
```

## Translation Updates
The `locale/es/LC_MESSAGES/django.po` file will be updated with the new `msgid` entries and their corresponding `msgstr` translations. Since `General` is currently empty, it will be populated.

After editing `.po` files, `python manage.py compilemessages` (or `django-admin compilemessages`) must be run to update the binary `.mo` files used by Django at runtime.
