from pydantic import BaseModel

from src.application.common import enumerations as enums

__all__ = [
    "UserType"
]


class UserType(BaseModel):
    user_type: enums.UserTypes
