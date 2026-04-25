# infrastructure Specification

## Purpose
TBD - created by archiving change setup-initial-dashboard. Update Purpose after archive.
## Requirements
### Requirement: Standardized API Pagination
The API SHALL return metadata-rich paginated responses including total count, current page, and total pages.

#### Scenario: Paginated API Response
- When requesting a list of items from a DRF endpoint.
- Then the response includes a `count` field and a `results` list.

### Requirement: Standardized Error Handling
The API SHALL return standardized error responses for all exceptions.

#### Scenario: API Error Response
- When an error occurs during an API request.
- Then the response contains `status: "error"`, a `message`, and `data`.

### Requirement: Custom Storage Backends
The project SHALL include custom storage backends for S3 to handle static and media files separately.

#### Scenario: Static Files on S3
- When `STORAGE_AWS=True`.
- Then static files are served from the `static/` location in the S3 bucket.

