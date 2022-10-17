from typing import Dict
from datetime import datetime

from sqlalchemy.orm import declared_attr
from sqlalchemy import MetaData, Column, DATETIME
from sqlalchemy.ext.declarative import as_declarative

__all__ = [
    "InoversityLibraryBase"
]


class_registry: Dict = {}


@as_declarative(
    class_registry=class_registry,
    metadata=MetaData(schema="InoversityLibraryModel")
)
class InoversityLibraryBase:
    insert_date = Column("insertDate", DATETIME, nullable=False, default=datetime.utcnow())
    __name__: str
    declarative_name_suffix = "Entity"

    # noinspection PyMethodParameters
    @declared_attr
    def __tablename__(cls) -> str:
        declarative_class_name = cls.__name__
        suffix = cls.declarative_name_suffix
        if declarative_class_name.endswith(suffix):
            declarative_class_name, *_ = cls.__name__.rsplit(suffix)
        return declarative_class_name
