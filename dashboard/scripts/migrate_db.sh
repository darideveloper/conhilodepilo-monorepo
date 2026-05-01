#!/bin/bash

# Exit on error
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DASHBOARD_DIR="$(dirname "$SCRIPT_DIR")"

# Ensure PYTHONPATH includes the venv packages to handle moved venvs
export PYTHONPATH=$PYTHONPATH:$DASHBOARD_DIR/venv/lib/python3.12/site-packages

# Function to log messages
log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Check for required tools
if ! command -v pg_dump &> /dev/null || ! command -v pg_restore &> /dev/null; then
    log_error "PostgreSQL tools (pg_dump, pg_restore) are required but not installed. Aborting."
    exit 1
fi

# Function to get a variable from an env file
get_env_var() {
    local file=$1
    local var=$2
    python3 -c "import os; from pathlib import Path; from dotenv import load_dotenv; load_dotenv('$file'); print(os.getenv('$var', ''))"
}

# --- SOURCE CONFIG (Local/Dev) ---
log_info "Loading source configuration from .env.dev..."
SRC_ENV=".env.dev"
SRC_DB_HOST=$(get_env_var "$SRC_ENV" "DB_HOST")
SRC_DB_PORT=$(get_env_var "$SRC_ENV" "DB_PORT")
SRC_DB_NAME=$(get_env_var "$SRC_ENV" "DB_NAME")
SRC_DB_USER=$(get_env_var "$SRC_ENV" "DB_USER")
SRC_DB_PASS=$(get_env_var "$SRC_ENV" "DB_PASSWORD")

SRC_DB_HOST=${SRC_DB_HOST:-localhost}
SRC_DB_PORT=${SRC_DB_PORT:-5432}

# --- TARGET CONFIG (Production) ---
log_info "Loading target configuration from .env.prod..."
TGT_ENV=".env.prod"
TGT_DB_HOST=$(get_env_var "$TGT_ENV" "DB_HOST")
TGT_DB_PORT=$(get_env_var "$TGT_ENV" "DB_PORT")
TGT_DB_NAME=$(get_env_var "$TGT_ENV" "DB_NAME")
TGT_DB_USER=$(get_env_var "$TGT_ENV" "DB_USER")
TGT_DB_PASS=$(get_env_var "$TGT_ENV" "DB_PASSWORD")
TGT_STORAGE_AWS=$(get_env_var "$TGT_ENV" "STORAGE_AWS")

TGT_DB_PORT=${TGT_DB_PORT:-5432}

# For media sync if needed
AWS_STORAGE_BUCKET_NAME=$(get_env_var "$TGT_ENV" "AWS_STORAGE_BUCKET_NAME")
AWS_PROJECT_FOLDER=$(get_env_var "$TGT_ENV" "AWS_PROJECT_FOLDER")

# Temporary file names
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOCAL_DUMP="local_dump_${TIMESTAMP}.sql"
PROD_BACKUP="prod_backup_before_migration_${TIMESTAMP}.bak"

# 1. Backup Production Database (Safety First)
log_info "Creating a safety backup of the production database..."
PGPASSWORD=$TGT_DB_PASS pg_dump -h "$TGT_DB_HOST" -p "$TGT_DB_PORT" -U "$TGT_DB_USER" -d "$TGT_DB_NAME" -F c -f "$PROD_BACKUP"
log_info "Production backup created: $PROD_BACKUP"

# 2. Export Local Database
log_info "Exporting local database to plain SQL..."
PGPASSWORD=$SRC_DB_PASS pg_dump -h "$SRC_DB_HOST" -p "$SRC_DB_PORT" -U "$SRC_DB_USER" -d "$SRC_DB_NAME" -F p -f "$LOCAL_DUMP"
log_info "Local database exported to $LOCAL_DUMP"

# 3. Import to Production
log_warn "Restoring data to production database. This will overwrite existing tables!"
read -p "Are you sure you want to continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    log_warn "Migration cancelled by user."
    exit 1
fi

log_info "Performing aggressive clean: dropping and recreating 'public' schema in production..."
PGPASSWORD=$TGT_DB_PASS psql -h "$TGT_DB_HOST" -p "$TGT_DB_PORT" -U "$TGT_DB_USER" -d "$TGT_DB_NAME" -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

log_info "Importing local SQL dump to production using psql..."
PGPASSWORD=$TGT_DB_PASS psql -h "$TGT_DB_HOST" -p "$TGT_DB_PORT" -U "$TGT_DB_USER" -d "$TGT_DB_NAME" -f "$LOCAL_DUMP" > /dev/null
log_info "Data imported to production successfully."

# 4. Media Synchronization
if [ "$TGT_STORAGE_AWS" == "True" ]; then
    log_info "Syncing media to AWS S3..."
    # Assuming aws-cli is configured or credentials are in .env.prod
    if command -v aws &> /dev/null; then
        aws s3 sync media/ "s3://${AWS_STORAGE_BUCKET_NAME}/${AWS_PROJECT_FOLDER}/media/" || log_warn "Media sync failed. Continuing with database steps."
    else
        log_warn "AWS CLI not found. Skipping S3 media sync. Please sync media manually."
    fi
else
    log_info "Production uses local storage. Media files should be transferred manually if not already present on the server."
fi

# 5. Post-Migration: Run Migrations and Reset Sequences
log_info "Running Django migrations and resetting sequences in production..."
cd "$DASHBOARD_DIR"
python3 manage.py migrate --noinput
log_info "Resetting sequences..."
# We need to pipe the output of sqlsequencereset to psql
# Better: just reset for 'booking' app which is the main one
python3 manage.py sqlsequencereset booking | PGPASSWORD=$TGT_DB_PASS psql -h "$TGT_DB_HOST" -p "$TGT_DB_PORT" -U "$TGT_DB_USER" -d "$TGT_DB_NAME"
log_info "Sequences reset for 'booking' app."

# 6. Verification
log_info "Verifying data in production..."
USER_COUNT=$(PGPASSWORD=$TGT_DB_PASS psql -h "$TGT_DB_HOST" -p "$TGT_DB_PORT" -U "$TGT_DB_USER" -d "$TGT_DB_NAME" -t -c "SELECT count(*) FROM auth_user;")
BOOKING_COUNT=$(PGPASSWORD=$TGT_DB_PASS psql -h "$TGT_DB_HOST" -p "$TGT_DB_PORT" -U "$TGT_DB_USER" -d "$TGT_DB_NAME" -t -c "SELECT count(*) FROM booking_booking;")
log_info "Production now has $USER_COUNT users and $BOOKING_COUNT bookings."

# 7. Cleanup
log_info "Cleaning up temporary dump files..."
rm "$LOCAL_DUMP"
# We keep the production backup for safety, but maybe delete old ones?
log_info "Migration completed successfully!"
log_warn "Note: $PROD_BACKUP was kept for safety. Delete it manually when confirmed."
