# Design: Database Migration Process

The migration process leverages standard PostgreSQL utilities (`pg_dump` and `psql`/`pg_restore`) to move data between environments.

## Architecture
The migration script will execute on a machine that has access to both the local and production databases (or can handle the transfer between them).

### 1. Environment Loading
The script will load source credentials from `.env.dev` and target credentials from `.env.prod`. To avoid variable name collisions and interactive prompts, we will use `PGPASSWORD` for each command.

### 2. Export Strategy
We will use the custom format (`-F c`) for `pg_dump`. This format is compressed and allows for more flexibility during restoration.

**Command Template:**
```bash
PGPASSWORD=$SOURCE_DB_PASSWORD pg_dump -h $SOURCE_DB_HOST -p $SOURCE_DB_PORT -U $SOURCE_DB_USER -d $SOURCE_DB_NAME -F c -f db_migration.bak
```

### 3. Import Strategy
Before importing, we MUST back up the target database. We will use `pg_restore` with the `--clean` and `--if-exists` flags.

**Command Template:**
```bash
PGPASSWORD=$TARGET_DB_PASSWORD pg_restore -h $TARGET_DB_HOST -p $TARGET_DB_PORT -U $TARGET_DB_USER -d $TARGET_DB_NAME --clean --if-exists --no-owner --no-privileges db_migration.bak
```
*Note: `--no-owner` and `--no-privileges` are critical when restoring to managed services (e.g., AWS RDS, Supabase, Neon) where the user might not have superuser rights.*

### 4. Connection Security (SSL)
Production databases often require SSL. The script should support `PGSSLMODE=require` if detected or needed.

### 5. Media Files Synchronization
Database migration only moves the pointers to media files. If `STORAGE_AWS=True` is used in production, media files must be uploaded to the S3 bucket. If production uses local storage, files in `backend/media/` must be transferred.

### 6. Sequence Synchronization
Django's `sqlsequencereset` is used to ensure that the ID sequences in PostgreSQL are updated to prevent "duplicate key" errors on future inserts.

**Command Template:**
```bash
python manage.py sqlsequencereset <app_name> | PGPASSWORD=$TARGET_DB_PASSWORD psql -h $TARGET_DB_HOST -p $TARGET_DB_PORT -U $TARGET_DB_USER -d $TARGET_DB_NAME
```

## Risks and Mitigations
- **Data Loss**: MANDATORY backup of the production database before any write operation.
- **Incompatible Versions**: Ensure `pg_dump` version matches or is newer than the source database, and `pg_restore` version matches or is newer than the target database.
- **Large Data**: For large media folders, use `aws s3 sync` or `rsync`.
