from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Union, Mapping, Any, AbstractSet, Dict, Type

from pydantic import BaseModel

__all__ = [
    "IntStr",
    "AbstractSetIntStr",
    "DictStrAny",
    "MappingIntStrAny",
    "AbstractDomainModel"
]


IntStr = Union[int, str]
AbstractSetIntStr = AbstractSet[IntStr]
DictStrAny = Dict[str, Any]
MappingIntStrAny = Mapping[IntStr, Any]


class AbstractDomainModel(BaseModel, ABC):
    """
    Abstract class for the domain models. The class inherits from a pydantic BaseModel which is used
    for parsing data used by the domain models. Any behaviour or attributes of the parent class to be
    used within the domain models must be redefined in this base class to avoid broken behaviour.
    """
    class Config:
        # This is redundant when the wrapping class does not inherit from pydantic's BaseModel
        orm_mode = True

    @classmethod
    @abstractmethod
    def from_orm(cls, obj) -> AbstractDomainModel:
        # Implement own 'from_orm' class method if not using the pydantic BaseModel.
        return super().from_orm(obj)

    @abstractmethod
    def dict(self, *args, **kwargs) -> DictStrAny:
        # Implement own 'dict' instance method if not using the pydantic BaseModel.
        return super().dict(*args, **kwargs)

    @classmethod
    @abstractmethod
    def parse_obj(cls: Type[AbstractDomainModel], obj: Any) -> AbstractDomainModel:
        # Implement own 'parse_obj' class method if not using the pydantic BaseModel.
        return super().parse_obj(obj=obj)
