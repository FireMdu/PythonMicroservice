from src.infrastructure.config.global_config.global_configuration import GlobalConfigurationManager
from src.data_access.database.databases_tools.connections.database_engines import MicrosoftSQLServerSQLAlchemy

__all__ = [
    "sql_server_connection"
]


configManager = GlobalConfigurationManager()
database_config = configManager.configuration.databases.main

sql_server_connection = MicrosoftSQLServerSQLAlchemy(
            server=database_config.server_name,
            server_port=database_config.server_port,
            database_name=database_config.database_name,
            database_uid=database_config.database_user,
            pwd=database_config.database_user_password
        )
