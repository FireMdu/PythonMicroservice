from sqlalchemy.orm import relationship
from sqlalchemy import Column, INTEGER, Identity, String, ForeignKey

from src.data_access.database.models.base_entity import InoversityLibraryBase

__all__ = [
    "UserEntity"
]


class UserEntity(InoversityLibraryBase):
    user_id = Column("id", INTEGER, Identity(), primary_key=True, index=True)
    first_name = Column("firstName", String(), nullable=False)
    last_name = Column("lastName", String(), nullable=False)
    email_address = Column("emailAddress", String(), nullable=False)
    password = Column("password", String(), nullable=False)
    user_type_id = Column("userTypeId", INTEGER(), ForeignKey("UserType.id"), nullable=False)
    account_id = Column("accountId", INTEGER(), ForeignKey("Account.id"), nullable=True)
    user_type_entity = relationship("UserTypeEntity", back_populates='user_entity')
    account_entity = relationship("AccountEntity", back_populates='user_entity', uselist=False)
