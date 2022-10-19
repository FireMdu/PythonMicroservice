from typing import List

from src.common.models.library_management.user import User, StudentUser
from src.common.models.library_management.user import user_types as enum_typ
from src.data_access.repositories.user_repository import UserSqlAlchemyRelationalRepository

__all__ = [
    "StudentUserSqlAlchemyRelationalRepository"
]


NO_IMPLEMENTATION = "No implementation"


class StudentUserSqlAlchemyRelationalRepository(UserSqlAlchemyRelationalRepository):
    def add(self, *, student: StudentUser) -> User:
        return super()._add_user(user=student, user_type=enum_typ.UserTypes.student)

    def list(self) -> List[User]:
        return super().list(enum_typ.UserTypes.student)

    def update(self, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def delete(self, id_):
        raise NotImplementedError(NO_IMPLEMENTATION)
