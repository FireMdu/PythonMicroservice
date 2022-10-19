from sqlalchemy.orm import relationship
from sqlalchemy import Column, INTEGER, Identity, String

from src.data_access.database.models.base_entity import InoversityLibraryBase

__all__ = [
    "UserTypeEntity"
]


class UserTypeEntity(InoversityLibraryBase):
    user_type_id = Column("id", INTEGER, Identity(), primary_key=True, index=True)
    user_type = Column("userType", String(256), nullable=False, unique=True)
    user_entity = relationship("UserEntity", back_populates='user_type_entity')
