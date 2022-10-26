#!/usr/bin/env bash

# Start SQL Server and Start the script to create the DB and user
/opt/mssql/bin/sqlservr & /usr/config/configure_db.sh
