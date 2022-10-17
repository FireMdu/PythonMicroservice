from typing import List

from pydantic import BaseModel

from src.application.models import Account
from src.services.library_management.student_service import ModelsService
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase

__all__ = [
    "AccountService",
]


class AccountService(ModelsService):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_all_accounts(repository: SqlAlchemyRelationalRepositoryBase, *args, **kwargs) -> List[Account]:
        return repository.list(*args, **kwargs)

    @staticmethod
    def post_an_account(repository: SqlAlchemyRelationalRepositoryBase, user, *args, **kwargs) -> BaseModel:
        account = repository.add(*args, user=user, **kwargs)
        return account
