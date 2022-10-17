from pydantic import BaseModel

from src.common.models.library_management.user import user_types as typ

__all__ = [
    "UserType"
]


class UserType(BaseModel):
    user_type: typ.UserTypes
