from typing import List

from pydantic import BaseModel

from src.common.models.library_management.user import User
from src.data_access.repositories.base_repository import RepositoryBase
from src.application.abstract_domain_service import AbstractDomainService

__all__ = [
    "UserService"
]


class UserService(AbstractDomainService):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_all_users(repository: RepositoryBase, *args, **kwargs) -> List[User]:
        return repository.list(*args, **kwargs)

    @staticmethod
    def post_user(
        repository: RepositoryBase,
        *args,
        **kwargs
    ) -> BaseModel:
        user = repository.add(*args, **kwargs)
        return user

    @staticmethod
    def get_user(
        repository: RepositoryBase,
        **filters
    ) -> BaseModel:
        user = repository.get(**filters)
        return user
