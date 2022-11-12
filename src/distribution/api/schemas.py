from pydantic import BaseModel

from src.data_access.context import ServiceContext

__all__ = [
    "PathDependency"
]


class PathDependency(BaseModel):
    context: ServiceContext

    class Config:
        arbitrary_types_allowed = True
