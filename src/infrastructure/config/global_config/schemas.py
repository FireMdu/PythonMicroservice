from typing import Union, Optional

from pydantic import BaseModel

__all__ = [
    "DatabaseDetails",
    "Databases",
    "GlobalConfiguration"
]


class DatabaseDetails(BaseModel):
    server_name: Optional[str]
    database_name: Optional[str]
    database_user: Optional[str]
    database_user_password: Optional[str]
    server_port: Union[str, None]

    class Config:
        fields = {
            "server_name": "serverName",
            "database_name": "databaseName",
            "database_user": "databaseUser",
            "database_user_password": "databaseUserPassword",
            "server_port": "serverPort"
        }


class Databases(BaseModel):
    main: DatabaseDetails = DatabaseDetails()


class GlobalConfiguration(BaseModel):
    databases: Databases = Databases()
