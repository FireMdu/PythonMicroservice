from abc import ABC, abstractmethod
from typing import TypeVar, Type, Optional, List

from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.data_access.database.models import InoversityLibraryBase

__all__ = [
    "EntityModel",
    "ApplicationModel",
    "RepositoryBase",
    "SqlAlchemyRelationalRepositoryBase"
]


EntityModel = TypeVar("EntityModel", bound=InoversityLibraryBase)
ApplicationModel = TypeVar("ApplicationModel", bound=BaseModel)


class RepositoryBase(ABC):
    def __init__(self, context: Session) -> None:
        self.context = context

    @abstractmethod
    def sync(self) -> None: ...

    @abstractmethod
    def add(self, *args, **kwargs) -> ApplicationModel: ...

    @abstractmethod
    def list(self, *args, **kwargs) -> ApplicationModel: ...

    @abstractmethod
    def get(self, **filters): ...

    @abstractmethod
    def update(self, **kwargs): ...

    @abstractmethod
    def delete(self, id_): ...


class SqlAlchemyRelationalRepositoryBase(RepositoryBase, ABC):
    def __init__(self, context: Session) -> None:
        self.relational_context: Session = context
        super().__init__(context=self.relational_context)

    def sync(self) -> None:
        self.context.flush()

    def add(
        self,
        *,
        entity_model: Type[EntityModel],
        app_model_instance: ApplicationModel,
        app_out_model: Type[ApplicationModel],
            **kwargs
    ) -> Optional[ApplicationModel]:
        entity = entity_model(**app_model_instance.dict())
        self.context.add(entity)
        self.sync()
        return app_out_model.from_orm(entity)

    def list(
        self,
        *,
        entity_model: Type[EntityModel],
        app_out_model: Type[ApplicationModel],
        **kwargs
    ) -> List[ApplicationModel]:
        entity_models = self.context.query(entity_model).all()
        return [app_out_model.from_orm(ele) for ele in entity_models]
