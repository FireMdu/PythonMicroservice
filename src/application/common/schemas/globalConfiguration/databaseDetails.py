from typing import Optional

from pydantic import BaseModel

__all__ = [
    "DatabaseDetails",
    "Databases"
]


class DatabaseDetails(BaseModel):
    serverName: Optional[str]
    databaseName: Optional[str]
    databaseUserId: Optional[str]
    databaseUserPassword: Optional[str]


class Databases(BaseModel):
    main: DatabaseDetails = DatabaseDetails()
    test: DatabaseDetails = DatabaseDetails()
    paymentProfileReader: DatabaseDetails = DatabaseDetails()
