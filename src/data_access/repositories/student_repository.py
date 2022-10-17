from typing import Optional

from src.common.models.library_management.user import User
from src.common.models.library_management.user import user_types as enum_typ
from src.data_access.repositories.user_repository import UserSqlAlchemyRelationalRepository

__all__ = [
    "StudentUserSqlAlchemyRelationalRepository"
]


NO_IMPLEMENTATION = "No implementation"


class StudentUserSqlAlchemyRelationalRepository(UserSqlAlchemyRelationalRepository):
    def add(self, *args, **kwargs) -> Optional[User]:
        return super().add_user(*args, user_type=enum_typ.UserTypes.student, **kwargs)

    def update(self, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def delete(self, id_):
        raise NotImplementedError(NO_IMPLEMENTATION)
