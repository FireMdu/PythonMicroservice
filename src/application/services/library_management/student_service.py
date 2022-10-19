from typing import List, Union

from src.common.models.library_management.user import StudentUser, User
from src.application.abstract_domain_service import AbstractDomainService
from src.data_access.repositories.student_repository import StudentUserSqlAlchemyRelationalRepository

__all__ = [
    "StudentService"
]


class StudentService(AbstractDomainService):
    def __init__(self, context) -> None:
        super().__init__(context=context)
        self.repository: StudentUserSqlAlchemyRelationalRepository = StudentUserSqlAlchemyRelationalRepository(
            context=self.context
        )

    def get_all_student_users(self) -> List[User]:
        return self.repository.list()

    def post_a_student_user(self, *, student: Union[StudentUser, User]) -> Union[StudentUser, User]:
        return self.repository.add(student=student)
