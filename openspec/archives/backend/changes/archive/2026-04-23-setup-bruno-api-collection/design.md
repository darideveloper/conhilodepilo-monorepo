# Design: Bruno API Integration

This document details the architectural decisions for integrating Bruno into the project, following the **Bruno v3 (OpenCollection YAML)** standard.

## Directory Structure
The Bruno collection will be located at the root in a `bruno/` directory.

```text
bruno/
├── environments/
│   ├── Local.yml
│   ├── Development.yml
│   └── Production.yml
├── Booking/
│   └── Get Company Config.yml    <-- GET /api/config/
└── opencollection.yml
```

### Rationale
- **Root Level:** Makes the collection highly discoverable and separates it from the Django application logic.
- **OpenCollection YAML Format:** As of Bruno v3, the `.yml` format is the modern, open-standard alternative to `.bru`. It is more Git-friendly and compatible with standard YAML tooling.
- **Environment Separation:** Environments allow switching between local development and hosted instances without modifying individual requests.
- **Feature-based Folders:** Organizing requests by Django app (e.g., `Booking/`) mirrors the backend structure.

## Environment Variables
Bruno environments will use the following standard variables:
- `base_url`: The root URL of the API (e.g., `http://localhost:8000`).

## Security
To prevent accidental exposure of secrets:
1.  **Strict `.gitignore`:** `bruno/.env` will be added to the project's `.gitignore`.
2.  **Secret Placeholders:** Environment files in Git will only contain non-sensitive configuration. Sensitive values must be provided via a local `bruno/.env` file or manual entry.

## Integration with CI/CD (Future)
The plain-text `.yml` files are natively supported by the Bruno CLI and standard YAML tools, facilitating automated testing in CI/CD pipelines.
