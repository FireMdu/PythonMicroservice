from typing import List

from src.common.models.library_management.user import StudentUser
from src.application.abstract_domain_service import AbstractDomainService
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase

__all__ = [
    "StudentService"
]


class StudentService(AbstractDomainService):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_all_students(repository: SqlAlchemyRelationalRepositoryBase, *args, **kwargs) -> List[StudentUser]:
        return repository.list(*args, **kwargs)

    @staticmethod
    def post_a_student(repository: SqlAlchemyRelationalRepositoryBase, *args, **kwargs) -> StudentUser:
        return repository.add(*args, **kwargs)
