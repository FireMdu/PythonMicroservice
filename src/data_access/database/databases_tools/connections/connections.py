from src.infrastructure.config.global_config.global_configuration import GlobalConfigurationManager
from src.data_access.database.databases_tools.connections.database_engines import MicrosoftSQLServerSQLAlchemy

__all__ = [
    "sql_server_connection"
]


configManager = GlobalConfigurationManager()
config = configManager.configuration
sql_server_connection = MicrosoftSQLServerSQLAlchemy(
            server=":".join([config.serverName, config.databasePort]),
            database_name=config.databaseName,
            database_uid=config.databaseUserId,
            pwd=config.databaseUserPassword
        )
