from typing import List

from src.common.models.library_management.account import Account
from src.application.abstract_domain_service import AbstractDomainService
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase

__all__ = [
    "AccountService",
]


class AccountService(AbstractDomainService):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_all_accounts(repository: SqlAlchemyRelationalRepositoryBase, *args, **kwargs) -> List[Account]:
        return repository.list(*args, **kwargs)

    @staticmethod
    def post_an_account(repository: SqlAlchemyRelationalRepositoryBase, *args, **kwargs) -> Account:
        account = repository.add(*args, **kwargs)
        return account
