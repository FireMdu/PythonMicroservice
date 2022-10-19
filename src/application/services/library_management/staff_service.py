from typing import List, Union

from src.common.models.library_management.user import Staff, User
from src.application.abstract_domain_service import AbstractDomainService
from src.data_access.repositories.staff_repository import StaffUserSqlAlchemyRelationalRepository

__all__ = [
    "StaffService"
]


class StaffService(AbstractDomainService):
    def __init__(self, context) -> None:
        super().__init__(context=context)
        self.repository: StaffUserSqlAlchemyRelationalRepository = StaffUserSqlAlchemyRelationalRepository(
            context=self.context
        )

    def get_all_staff_users(self) -> List[User]:
        return self.repository.list()

    def post_a_staff_user(self, *, staff: Union[Staff, User]) -> Union[Staff, User]:
        return self.repository.add(staff=staff)
