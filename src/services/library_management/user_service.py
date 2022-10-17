from abc import ABC
from typing import List, Union

from pydantic import BaseModel

from src.application.common import enumerations as enums
from src.application.models.library_management.user import User
from src.data_access.repositories.base_repository import RepositoryBase

__all__ = [
    "UserService",
    "ModelsService"
]


class ModelsService(ABC):
    def __init__(self) -> None: ...


class UserService(ModelsService):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_all_users(repository: RepositoryBase, *args, **kwargs) -> List[User]:
        return repository.list(*args, **kwargs)

    @staticmethod
    def post_user(
        repository: RepositoryBase,
        user_type: Union[enums.UserTypes, str],
        *args,
        **kwargs
    ) -> BaseModel:
        user = repository.add(user_type=user_type, *args, **kwargs)
        return user

    @staticmethod
    def get_user(
        repository: RepositoryBase,
        **filters
    ) -> BaseModel:
        user = repository.get(**filters)
        return user
