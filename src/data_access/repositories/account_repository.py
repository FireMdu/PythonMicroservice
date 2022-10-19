import random
import string
from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound

from src.data_access.database.models.users import UserEntity
from src.common.models.library_management.account import Account
from src.data_access.database.models.account_entity import AccountEntity
from src.common.models.library_management.account import AccountInDatabase
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase
from src.common.models.library_management.exceptions import NoneExistingAccount, NoneUniqueExistingAccount

__all__ = [
    "AccountSqlAlchemyRelationalRepository"
]


NO_IMPLEMENTATION = "No implementation"


class AccountSqlAlchemyRelationalRepository(SqlAlchemyRelationalRepositoryBase):
    def __init__(self, context: Session) -> None:
        super().__init__(context=context)

    def create(self, *, user_email_address: str) -> Optional[Account]:
        try:
            user: UserEntity = self.context.query(UserEntity).filter_by(email_address=user_email_address).scalar()
        except MultipleResultsFound:
            raise NoneUniqueExistingAccount()
        if user is None:
            raise NoneExistingAccount()
        if user.account_entity is not None:
            return Account.from_orm(user.account)
        account_model = AccountInDatabase(account_number=self.generate_account_number(length=10))
        account_entity = AccountEntity(user_entity=user, **account_model.dict())
        self.context.add(account_entity)
        self.sync()
        return Account.from_orm(account_entity)

    def add(self, *args, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    @staticmethod
    def generate_account_number(*, length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def list(self) -> List[Account]:
        accounts: Optional[List[AccountEntity]] = self.context.query(AccountEntity).all()
        if accounts is None:
            return []
        return [Account.from_orm(ele) for ele in accounts]

    def get(self, **filters):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def update(self, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def delete(self, id_):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def get_teachers(self):
        ...
