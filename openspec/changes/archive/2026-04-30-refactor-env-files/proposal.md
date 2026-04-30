# Proposal: Refactor Environment Variables

**Change ID:** refactor-env-files
**Scope:** Architecture / Configuration
**Status:** Draft

## Objective
Standardize the environment variable loading strategy across all services (`backend`, `booking`, `landing`) in the monorepo. The core rule is that the `.env` file should serve exclusively to declare the active environment (`ENV=prod` or `ENV=dev`), while all context-specific configuration lives in dedicated files (`.env.dev` and `.env.prod`).

## Context
Currently, the backend has implemented a rudimentary version of this two-tier environment system, but there is still bleed-over in `.env` and `.env.example` files. The `landing` and `booking` applications lack this structure entirely and rely on a monolithic `.env` configuration. This leads to inconsistency in how environments are defined and loaded, risking configuration leaks or setup complexity for developers.

## Scope of Changes
1. **Central Rule:** The `.env` file must only contain `ENV=dev` or `ENV=prod`.
2. **Dedicated Environment Files:** All other secrets, endpoints, and configuration must reside in `.env.dev` or `.env.prod`.
3. **Example Templates:** Every `.env` format must have a corresponding `.example` file (e.g., `.env.example`, `.env.dev.example`, `.env.prod.example`) in all three apps, containing zero sensitive data.
4. **App Initialization Logic:** Update Astro configurations (`booking` and `landing`) and Django settings (`backend`) to explicitly parse `.env` to determine `ENV`, and subsequently load the respective `.env.${ENV}` file.
5. **Migrate Real Files:** Migrate the actual local `.env` files in all three apps by backing them up, safely moving their values to `.env.dev` and `.env.prod`, and stripping the root `.env` down to just `ENV=dev` (or `ENV=prod`).

## Technical Considerations
- In `backend/project/settings.py`, the existing `dotenv` configuration already partially loads `.env.${ENV}`. We need to ensure `.env.example` represents only `ENV=dev` and that the `.env.dev.example` / `.env.prod.example` templates cover all necessary variables.
- In `booking` and `landing`, Astro natively delegates to Vite for environment variables via `import.meta.env`. Vite typically expects `.env.development` or `.env.production` based on the `mode`. We will need to intercept this by explicitly using `dotenv` in `astro.config.mjs` (or similar bootstrap files) to map `ENV` to the load logic, satisfying the monorepo's shared `ENV=dev|prod` convention while seamlessly feeding those variables into the build process.
- **Build & Deployment Tooling:** Variables related to build packs or deployment environments (such as `NIXPACKS_NIXPKGS` or `NIXPACKS_NODE_VERSION` found in `booking/.env`) might need to be set in the deployment provider's dashboard directly rather than relying on local `.env` files during CI/CD, since the local `.env` will now only define the `ENV` context.