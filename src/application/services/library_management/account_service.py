from typing import List

from src.common.models.library_management.account import Account
from src.application.abstract_domain_service import AbstractDomainService
from src.data_access.repositories.account_repository import AccountSqlAlchemyRelationalRepository

__all__ = [
    "AccountService",
]


class AccountService(AbstractDomainService):

    def __init__(self, context) -> None:
        super().__init__(context)
        self.repository: AccountSqlAlchemyRelationalRepository = AccountSqlAlchemyRelationalRepository(
            context=self.context
        )

    def get_all_accounts(self) -> List[Account]:
        return self.repository.list()

    def create_account_for_user(self, *, user_email_address) -> Account:
        return self.repository.create(user_email_address=user_email_address)
