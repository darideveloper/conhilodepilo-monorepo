# admin-ui Specification Delta

## MODIFIED Requirements

### Requirement: Modern Admin Interface
The project SHALL use `django-unfold` to provide a modern, Tailwind-based administrative interface.

#### Scenario: Access Admin Dashboard
- When a superuser logs into `/admin/`.
- Then the interface uses the Unfold theme with custom primary colors and the site title is "Con Hilo Depilo".
- And the sidebar navigation is organized into the following sections:
    - **Autenticación:** Usuarios, Grupos.
    - **Gestión:** Reservas, Servicios.
    - **Configuración:** Disponibilidad, Perfil de Empresa.
- And each navigation item has an appropriate Material Icon.

#### Scenario: Navigate to Business Modules
- Given the superuser is on the admin dashboard.
- When they click "Reservas" in the sidebar.
- Then they are redirected to the Booking changelist.
- When they click "Perfil de Empresa" in the sidebar.
- Then they are redirected to the Company Profile change form (Singleton).
