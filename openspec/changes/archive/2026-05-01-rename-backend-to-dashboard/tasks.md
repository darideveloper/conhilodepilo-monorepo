## 1. Directory Rename
- [x] 1.1 Rename `backend/` directory to `dashboard/`

## 2. Root Script and File Updates
- [x] 2.1 Update `dev.sh` to reference `dashboard/` and rename tmux window
- [x] 2.2 Update `README.md` structure, installation steps, and service descriptions
- [x] 2.3 Update `.gitignore` in root if it has `backend/` specific rules
- [x] 2.4 Update `CLAUDE.md` if it references the `backend` directory

## 3. Documentation Updates (OpenSpec)
- [x] 3.1 Update `openspec/project.md` service definitions and directory fields
- [x] 3.2 Update `dashboard/AGENTS.md` and root `AGENTS.md`
- [x] 3.3 Bulk update `openspec/` directory paths (search/replace `backend/` with `dashboard/` in all `.md` files)
- [x] 3.4 Verify and update paths in `openspec/specs/api-contracts/backend-v1.md` (if it exists or is referenced)

## 4. Internal Dashboard Updates
- [x] 4.1 Update `dashboard/scripts/migrate_db.sh` logs and internal comments
- [x] 4.2 Check `dashboard/project/wsgi.py` and `asgi.py` for any hardcoded project name or path comments
- [x] 4.3 Check `dashboard/manage.py` for any "backend" specific comments or custom environment loading logic
- [x] 4.4 Update `dashboard/.env.dev.example` and `.env.prod.example` comments if they reference "backend"

## 5. Frontend References
- [x] 5.1 Rename types in `booking/src/lib/api/endpoints/services.ts` (BackendService -> DashboardService)
- [x] 5.2 Search for "backend" strings in `booking/` and `landing/` to ensure no local dev URLs are broken
