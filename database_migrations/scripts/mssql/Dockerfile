FROM mcr.microsoft.com/mssql/server:2019-CU18-ubuntu-20.04

# Create a config directory
RUN mkdir -p /usr/config
WORKDIR /usr/config

# Bundle config source
COPY . /usr/config

COPY initialize_db.sql initialize_db.sql
COPY configure_db.sh configure_db.sh
COPY entrypoint.sh entrypoint.sh

EXPOSE 1433
ENTRYPOINT ["./entrypoint.sh"]
