from sqlalchemy.orm import sessionmaker

from src.data_access.database.databases_tools.connections.connections import sql_server_connection

__all__ = [
    "relational_database_context"
]


relational_database_context = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sql_server_connection.connection
)
