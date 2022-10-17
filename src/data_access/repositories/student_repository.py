from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound

from src.data_access.database.models.student_entity import StudentEntity
from src.application.models.library_management.user import StudentUser, StudentUserInDatabase
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase

__all__ = [
    "StudentSqlAlchemyRelationalRepository"
]


NO_IMPLEMENTATION = "No implementation"


class StudentSqlAlchemyRelationalRepository(SqlAlchemyRelationalRepositoryBase):
    def __init__(self, context: Session) -> None:
        super().__init__(context=context)

    def add(self, *args, **kwargs) -> Optional[StudentUser]:
        entity = StudentEntity(**StudentUserInDatabase.parse_obj(kwargs).dict())
        try:
            db_student = self.context.query(StudentEntity)
            db_student = db_student.filter(StudentEntity.student_number == entity.student_number).scalar()
            if db_student is not None:
                return StudentUserInDatabase.from_orm(db_student)
        except MultipleResultsFound:
            return StudentUserInDatabase.from_orm(entity)
        else:
            self.context.add(entity)
            self.sync()
        return StudentUserInDatabase.from_orm(entity)

    def list(self, *args, **kwargs) -> List[StudentUser]:
        return super().list(*args, entity_model=StudentEntity, app_out_model=StudentUser, **kwargs)

    def get(self, **filters):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def update(self, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def delete(self, id_):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def get_teachers(self):
        ...
