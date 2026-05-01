# Tasks: Database Migration

## Phase 1: Preparation
- [x] Check for presence of `pg_dump` and `pg_restore` on the host machine. <!-- id: 10 -->
- [x] Create `dashboard/scripts/` directory. <!-- id: 0 -->
- [x] Create `dashboard/scripts/migrate_db.sh` with environment loading logic. <!-- id: 1 -->
- [x] Add `*.bak` and `*.sql` to `dashboard/.gitignore`. <!-- id: 2 -->

## Phase 2: Safety First
- [x] Implement a pre-migration backup of the production database in `migrate_db.sh`. <!-- id: 11 -->

## Phase 3: Data Migration Logic
- [x] Implement local database export in `migrate_db.sh`. <!-- id: 3 -->
- [x] Implement production database import in `migrate_db.sh`. <!-- id: 4 -->

## Phase 4: Media Synchronization
- [x] Add logic to sync `dashboard/media/` to production (S3 or remote path). <!-- id: 12 -->

## Phase 5: Post-Migration Consistency
- [x] Add step to run `python manage.py migrate` in production. <!-- id: 5 -->
- [x] Add step to reset PostgreSQL sequences using `sqlsequencereset`. <!-- id: 6 -->

## Phase 6: Validation and Cleanup
- [x] Add verification check (e.g., count users or bookings). <!-- id: 13 -->
- [x] Add cleanup logic to remove local dump files. <!-- id: 7 -->

## Phase 7: Execution (Manual)
- [x] Run `migrate_db.sh` and capture output (excluding secrets). <!-- id: 8 -->
- [x] Verify production site is fully functional. <!-- id: 9 -->
