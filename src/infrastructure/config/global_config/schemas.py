from typing import Optional

from pydantic import BaseModel

__all__ = [
    "DatabaseDetails",
    "Databases",
    "GlobalConfiguration"
]


class DatabaseDetails(BaseModel):
    serverName: Optional[str]
    databaseName: Optional[str]
    databaseUserId: Optional[str]
    databaseUserPassword: Optional[str]


class Databases(BaseModel):
    main: DatabaseDetails = DatabaseDetails()


class GlobalConfiguration(BaseModel):
    databases: Databases
