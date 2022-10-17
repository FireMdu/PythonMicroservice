import os

from src.common.config.global_config.global_configuration import GlobalConfigurationManager
from src.data_access.database.databases_tools.connections.database_engines import MicrosoftSQLServerSQLAlchemy

__all__ = [
    "sql_server_connection"
]


configManager = GlobalConfigurationManager()
config = configManager.configuration
sql_server_connection = MicrosoftSQLServerSQLAlchemy(
            server=os.environ.get(config.databases.main.serverName),
            database_name=os.environ.get(config.databases.main.databaseName),
            database_uid=os.environ.get(config.databases.main.databaseUserId),
            pwd=os.environ.get(config.databases.main.databaseUserPassword)
        )
