from sqlalchemy import Column, INTEGER, Identity, String

from src.data_access.database.models.base_entity import InoversityLibraryBase

__all__ = [
    "StaffEntity"
]


class StaffEntity(InoversityLibraryBase):
    user_id = Column("id", INTEGER, Identity(), primary_key=True, index=True)
    role_level = Column("roleLevel", String(256), nullable=False, index=True)
    staff_number = Column("staffNumber", String(20), nullable=False, unique=True)
    department = Column("department", String(100), nullable=False)
    job_title = Column("jobTitle", String(100), nullable=False)
