from pathlib import Path

from pydantic import BaseModel, BaseSettings, Field

from src.app_definitions import ROOT_DIR

__all__ = [
    "DatabaseDetails",
    "Databases",
    "GlobalConfiguration"
]


class DatabaseDetails(BaseSettings):
    serverName: str = Field(..., env="DATABASE_HOST_NAME")
    databaseName: str = Field(..., env="DATABASE_NAME")
    databaseUserId: str = Field(..., env="DATABASE_LIB_ADMIN_USER_ID")
    databaseUserPassword: str = Field(..., env="DATABASE_LIB_ADMIN_PASSWORD")
    databasePort: str = Field(..., env="DATABASE_PORT")

    class Config:
        env_file = ROOT_DIR.joinpath(Path(".env"))


class Databases(BaseModel):
    main: DatabaseDetails = DatabaseDetails()


class GlobalConfiguration(BaseModel):
    databases: Databases = Databases()
