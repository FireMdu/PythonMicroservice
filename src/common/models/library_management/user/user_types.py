from enum import Enum

__all__ = [
    "UserTypes"
]


class UserTypes(str, Enum):
    student: str = "Student"
    staff: str = "Staff"
