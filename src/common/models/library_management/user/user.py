from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, List, Union, Mapping, Any, AbstractSet, Dict, Type

from src.common.models.library_management.account import Account
from src.common.models.library_management.base_model import AbstractDomainModel
from src.common.models.library_management.document import Document

__all__ = [
    "User",
    "UserInDatabase",
    "StudentUser",
    "StudentUserInDatabase",
    "Staff"
]

IntStr = Union[int, str]
AbstractSetIntStr = AbstractSet[IntStr]
DictStrAny = Dict[str, Any]
MappingIntStrAny = Mapping[IntStr, Any]


class UserBase(AbstractDomainModel, ABC):
    """
    Represents a user model and all the behaviours to be associated with a user type object.
    """
    first_name: str
    last_name: str
    email_address: str

    def __hash__(self):
        return hash(self.user_identifier)

    def __eq__(self, other):
        if isinstance(other, User):
            return other.user_identifier == self.user_identifier
        return False

    @classmethod
    def from_orm(cls, obj) -> UserBase:
        return super().from_orm(obj=obj)

    @classmethod
    def parse_obj(cls: Type[UserBase], obj: Any) -> Union[UserBase, AbstractDomainModel]:
        return super().parse_obj(obj=obj)

    def dict(
        self,
        *,
        include: Union[AbstractSetIntStr, Mapping[IntStr, Any]] = None,
        exclude: Union[AbstractSetIntStr, Mapping[IntStr, Any]] = None,
        by_alias: bool = False,
        skip_defaults: bool = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ) -> DictStrAny:
        return super().dict(
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none
        )

    @property
    @abstractmethod
    def user_identifier(self) -> str: ...

    @abstractmethod
    def verify(self) -> None: ...

    @abstractmethod
    def check_account(self) -> Account: ...

    def is_valid_user(self, users: List[User]) -> bool:
        if any([self == user for user in users]):
            return True
        return False


class User(UserBase):
    @property
    def user_identifier(self) -> str:
        return self.email_address

    def verify(self) -> None:
        ...

    def get_documents(self, status: str) -> List[Document]:
        ...

    def check_account(self) -> Account:
        ...


class UserInDatabase(User):
    user_id: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True


class StudentUser(User):
    student_number: str
    faculty: str
    school: str
    programme: str

    class Config:
        orm_mode = True

    @property
    def user_identifier(self) -> str:
        return self.student_number

    def verify(self) -> None:
        ...

    def get_documents(self, status: str) -> List[Document]:
        ...

    def check_account(self) -> Account:
        ...


class StudentUserInDatabase(StudentUser):
    user_id: Optional[int]
    password: Optional[str]

    class Config:
        orm_mode = True


class Staff(User):
    staff_number: str
    department: str
    job_title: str

    @property
    def user_identifier(self) -> str:
        return self.staff_number

    def verify(self) -> None:
        ...

    def get_documents(self, status: str) -> List[Document]:
        ...

    def check_account(self) -> Account:
        ...


class Alumni(User):
    alumni_number: str

    @property
    def user_identifier(self) -> str:
        return self.alumni_number

    def verify(self) -> None:
        ...

    def get_documents(self, status: str) -> List[Document]:
        ...

    def check_account(self) -> Account:
        ...
