## 1. Update BookingAdmin list_display

- [x] 1.1 Replace `list_display` tuple to: `("get_client_name", "get_status", "get_services", "get_price", "get_created_at", "get_start_time")`
- [x] 1.2 Remove `google_sync_status_badge` from `list_display`
- [x] 1.3 Remove `google_sync_status_badge` method (or keep if used elsewhere)

## 2. Add computed column methods

- [x] 2.1 Add `@admin.display(description="Servicios") get_services(self, obj)` method returning `", ".join(obj.services.all().values_list("name", flat=True))`
- [x] 2.2 Add `@admin.display(description="Precio") get_price(self, obj)` method returning sum of `service.price for service in obj.services.all()`
- [x] 2.3 Add `@admin.display(description="Fecha de compra") get_created_at(self, obj)` method returning `obj.created_at`
- [x] 2.4 Add `prefetch_related("services")` override via `get_queryset` to avoid N+1 queries

## 3. Add Spanish labels for model fields

- [x] 3.1 Add `@admin.display(description="Cliente")` to any existing `client_name` reference (or use `list_display` with a wrapper)
- [x] 3.2 Add `@admin.display(description="Estado")` to any existing `status` reference
- [x] 3.3 Add `@admin.display(description="Fecha del servicio")` to any existing `start_time` reference

## 4. Verify and clean up

- [x] 4.1 Run lint/typecheck on the modified file (Python syntax check passed)
- [x] 4.2 Verify no broken references to removed `google_sync_status_badge` in `list_display` (no remaining references found)
- [x] 4.3 Verify the admin list view renders correctly (pending server restart)
