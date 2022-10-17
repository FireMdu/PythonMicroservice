from pydantic import BaseModel

from src.application.common.schemas.globalConfiguration.databaseDetails import Databases

__all__ = [
    "GlobalConfiguration"
]


class GlobalConfiguration(BaseModel):
    databases: Databases
