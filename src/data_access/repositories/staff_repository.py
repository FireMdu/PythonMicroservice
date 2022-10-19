from typing import Optional, List

from src.common.models.library_management.user import User, Staff
from src.common.models.library_management.user import user_types as enum_typ
from src.data_access.repositories.user_repository import UserSqlAlchemyRelationalRepository

__all__ = [
    "StaffUserSqlAlchemyRelationalRepository"
]


NO_IMPLEMENTATION = "No implementation"


class StaffUserSqlAlchemyRelationalRepository(UserSqlAlchemyRelationalRepository):
    def add(self, staff: Staff) -> Optional[User]:
        return super()._add_user(user=staff, user_type=enum_typ.UserTypes.staff)

    def list(self) -> List[User]:
        return super().list(enum_typ.UserTypes.staff)

    def update(self, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def delete(self, id_):
        raise NotImplementedError(NO_IMPLEMENTATION)
