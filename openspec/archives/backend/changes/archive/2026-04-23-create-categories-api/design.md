# Design Notes

## Data Mapping & Representation
The `GET /api/services/` response will map directly to the `EventType` and `Event` models in `booking/models.py`.

### Category (EventType) Representation
The root elements of the JSON response array will map to `EventType` instances.
- `id`: The primary key.
- `name`: The `name` field.
- `description`: The `description` field.
- `image`: Absolute URL to the uploaded image.

### Service (Event) Representation
Each category will have a `services` array, mapping to `Event` instances related via the `event_type` foreign key.
- `id`: The primary key.
- `title`: Maps to the `name` field of the `Event` model.
- `description`: The `description` field.
- `price`: Decimal formatted as a string.
- `duration`: Maps to `duration_minutes`.
- `image`: Absolute URL to the uploaded image.

## Caching Strategy (Future)
Since this catalog data rarely changes compared to the availability slots, separating this endpoint from the availability data allows for aggressive HTTP caching or CDN integration in the future, improving frontend load times.

## Avoid N+1 Queries
When querying the `EventType` models in the DRF View, we must use `.prefetch_related('events')` to load all nested services efficiently in a single query, preventing the N+1 query problem during serialization.
