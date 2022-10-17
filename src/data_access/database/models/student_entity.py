from sqlalchemy import Column, INTEGER, Identity, String

from src.data_access.database.models.base_entity import InoversityLibraryBase


class StudentEntity(InoversityLibraryBase):
    user_id = Column("id", INTEGER, Identity(), primary_key=True, index=True)
    role_level = Column("roleLevel", String(256), nullable=False, index=True)
    student_number = Column("studentNumber", String(20), nullable=False, unique=True)
    faculty = Column("faculty", String(), nullable=False)
    school = Column("school", String(), nullable=False)
    programme = Column("programme", String(), nullable=False)
