# Design: Company Configuration API

## Architecture Overview
The solution leverages the existing `django-solo` singleton model and `djangorestframework` to provide a lightweight, cached, and public endpoint.

## Component Details

### 1. Model Enhancements (`booking/models.py`)
Add fields to `CompanyProfile` to support the labels documented in `docs/api.md`:
- `event_type_label` (default: "Service Category")
- `event_label` (default: "Consultation")
- `availability_free_label` (default: "Available")
- `availability_regular_label` (default: "Partial")
- `availability_no_free_label` (default: "Fully Booked")
- `extras_label` (default: "Add-ons")

### 2. Serializer (`booking/serializers.py`)
A `ModelSerializer` will handle:
- Automatic URL resolution for the `logo` ImageField using DRF's context.
- Mapping model fields to the exact JSON keys defined in the API spec.

### 3. API View (`booking/views.py`)
A subclass of `rest_framework.views.APIView` will:
- Fetch the singleton instance using `CompanyProfile.get_solo()`.
- Explicitly set `permission_classes = [AllowAny]` for public access.
- Inject the system `TIME_ZONE` from settings into the response.

### 4. Routing (`project/urls.py`)
Manual registration of the `/api/config/` path to avoid router-induced pluralization or complex viewset logic for a single-object endpoint.

## Data Flow
1. Client sends `GET /api/config/`.
2. View fetches the `CompanyProfile` singleton.
3. Serializer converts the model and generates absolute URLs for assets.
4. Response is returned with `200 OK`.

## Trade-offs
- **APIView vs ViewSet:** Using `APIView` is preferred over a `ViewSet` because we are dealing with a singleton (one object), and standard CRUD operations (POST, PUT, DELETE) are not exposed publicly.
