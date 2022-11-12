from datetime import datetime

from sqlalchemy.orm import relationship
from sqlalchemy import Column, INTEGER, Identity, String, DATETIME, Boolean

from src.data_access.database.models.base_entity import InoversityLibraryBase

__all__ = [
    "AccountEntity"
]


class AccountEntity(InoversityLibraryBase):
    account_id = Column("id", INTEGER, Identity(), primary_key=True, index=True)
    account_number = Column("accountNumber", String(20), nullable=False, index=True, unique=True)
    active = Column("active", Boolean, default=True)
    registration_date = Column("registrationDate", DATETIME, default=datetime.utcnow())
    user_entity = relationship("UserEntity", back_populates='account_entity', uselist=False)
