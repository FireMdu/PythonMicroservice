from typing import List, Optional

from src.common.models.library_management.user import User
from src.application.abstract_domain_service import AbstractDomainService
from src.common.models.library_management.user import user_types as enum_type
from src.data_access.repositories.user_repository import UserSqlAlchemyRelationalRepository

__all__ = [
    "UserService"
]


class UserService(AbstractDomainService):
    def __init__(self, context) -> None:
        super().__init__(context)
        self.repository: UserSqlAlchemyRelationalRepository = UserSqlAlchemyRelationalRepository(context=self.context)

    def get_all_users(self) -> List[User]:
        return self.repository.list(enum_type.UserTypes.student, enum_type.UserTypes.staff)

    def get_user_by_filters(self, **filters) -> Optional[User]:
        return self.repository.get(**filters)
