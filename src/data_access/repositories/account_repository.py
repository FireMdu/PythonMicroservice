from typing import Optional, Union

from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.orm import Session

from src.common.models import Account, User
from src.data_access.database import AccountEntity
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase

__all__ = [
    "AccountSqlAlchemyRelationalRepository"
]


NO_IMPLEMENTATION = "No implementation"


class AccountSqlAlchemyRelationalRepository(SqlAlchemyRelationalRepositoryBase):
    def __init__(self, context: Session) -> None:
        super().__init__(context=context)

    def add(self, *args, user: Union[User], **kwargs) -> Optional[Account]:
        entity = AccountEntity(user=user, **Account.parse_obj(kwargs).dict())
        try:
            # check if user has a valid account already
            user_account = user.account
            if user_account is not None:
                return Account.from_orm(entity)
        except MultipleResultsFound:
            return Account.from_orm(entity)
        else:
            self.context.add(entity)
            self.sync()
        return Account.from_orm(entity)

    def get(self, **filters):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def update(self, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def delete(self, id_):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def get_teachers(self):
        ...
