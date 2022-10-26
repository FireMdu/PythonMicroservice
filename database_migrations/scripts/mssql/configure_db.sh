#!/bin/bash

# Wait 600 (default) seconds for SQL Server to start up by ensuring that
# calling SQLCMD does not return an error code, which will ensure that sqlcmd is accessible
# and that system and user databases return "0" which means all databases are in an "online" state

# constants
ROOT_DIR="$(cd ../../../; pwd)"

# variables

# set all environment variables from the .env file
# shellcheck disable=SC2046
export $(grep -v '^#' "$ROOT_DIR/.env" | xargs)

# Run the setup script for database initialization tasks
sleep 20

/opt/mssql-tools/bin/sqlcmd -S $DATABASE_HOST_NAME -U $DATABASE_SA_USER_ID -P $DATABASE_SA_PASSWORD -i initialize_db.sql -e

exit
