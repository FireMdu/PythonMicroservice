from abc import ABC
from typing import List

from pydantic import BaseModel

from src.application.models.library_management.user import StudentUser
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase

__all__ = [
    "StudentService",
    "ModelsService"
]


class ModelsService(ABC):
    def __init__(self) -> None: ...


class StudentService(ModelsService):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_all_students(repository: SqlAlchemyRelationalRepositoryBase, *args, **kwargs) -> List[StudentUser]:
        return repository.list(*args, **kwargs)

    @staticmethod
    def post_a_student(repository: SqlAlchemyRelationalRepositoryBase, *args, **kwargs) -> BaseModel:
        student = repository.add(*args, **kwargs)
        return student
