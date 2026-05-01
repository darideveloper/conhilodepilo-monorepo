# Tasks: Consolidate Host Configuration

- [x] **Research & Validation**
    - [x] Confirm no other hidden usages of `SITE_URL` exist in the dashboard.
    - [x] Verify if any frontend components rely on the dashboard's `SITE_URL` via an API response.

- [x] **Implementation**
    - [x] **Settings Refactor**: Modify `dashboard/project/settings.py` to:
        - Add `HOST = os.getenv("HOST")`.
        - Remove `SITE_URL = os.getenv("SITE_URL")`.
        - Add logic to automatically include `HOST` hostname in `ALLOWED_HOSTS`.
    - [x] **Stripe Utils Update**: Modify `dashboard/utils/stripe_utils.py` to use `settings.HOST`.
    - [x] **Dockerfile Update**: Add `HOST` to `dashboard/Dockerfile` as an `ARG` and `ENV`.
    - [x] **Environment Cleanup**:
        - [x] Update `dashboard/.env.dev` (Remove `SITE_URL`).
        - [x] Update `dashboard/.env.prod` (Remove `SITE_URL`).
        - [x] Update `dashboard/.env.dev.example` (Remove `SITE_URL`).
        - [x] Update `dashboard/.env.prod.example` (Remove `SITE_URL`).

- [x] **Verification**
    - [x] Run dashboard tests to ensure `media.py` and `stripe_utils.py` don't break.
    - [x] Manually verify a media URL generation (via `python manage.py shell`).
    - [x] Verify `ALLOWED_HOSTS` includes the `HOST` hostname.
    - [x] Run `openspec validate consolidate-host-config --strict`.
