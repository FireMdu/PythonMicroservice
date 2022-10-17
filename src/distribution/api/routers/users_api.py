from typing import TypeVar, List, Optional

from pydantic import BaseModel
from fastapi import APIRouter, Depends
from fastapi_versioning import version

from src.data_access.context import ServiceContext
from src.data_access.database import SqlAlchemyContext
from src.data_access.repositories.base_repository import RepositoryBase
from src.application.services.library_management import UserService
from src.common.models.library_management.user import User, UserInDatabase
from src.data_access.repositories.user_repository import UserSqlAlchemyRelationalRepository
from src.data_access.repositories.student_repository import StudentUserSqlAlchemyRelationalRepository
from src.data_access.repositories.staff_repository import StaffUserSqlAlchemyRelationalRepository


Repository = TypeVar("Repository", bound=RepositoryBase)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


class PathDependency(BaseModel):
    context: ServiceContext

    class Config:
        arbitrary_types_allowed = True


def sqlalchemy_dependency():
    yield PathDependency(context=SqlAlchemyContext())


@router.get("/", status_code=200, name="Get all users", response_model=List[User])
@version(1, 0)
async def get_all_users(path_dependency: PathDependency = Depends(sqlalchemy_dependency)):
    with path_dependency.context.get_context() as context:
        user_repository = UserSqlAlchemyRelationalRepository(context=context)
        users = UserService.get_all_users(repository=user_repository)
        return users


@router.post("/student", name="Post student user", status_code=200, response_model=User)
@version(1, 0)
async def post_student(
        student: UserInDatabase,
        path_dependency: PathDependency = Depends(sqlalchemy_dependency)
):
    with path_dependency.context.get_context() as context:
        user_repository = StudentUserSqlAlchemyRelationalRepository(context=context)
        student = UserService.post_user(repository=user_repository, **student.dict())
        return User.parse_obj(student.dict())


@router.post("/staff", name="Post staff user", status_code=200, response_model=User)
@version(1, 0)
async def post_staff(
        staff: UserInDatabase,
        path_dependency: PathDependency = Depends(sqlalchemy_dependency)
):
    with path_dependency.context.get_context() as context:
        user_repository = StaffUserSqlAlchemyRelationalRepository(context=context)
        staff = UserService.post_user(repository=user_repository, **staff.dict())
        return User.parse_obj(staff.dict())


@router.get(
    "/{email_address}",
    name="Get user by email address",
    status_code=200,
    response_model=Optional[User]
)
@version(1, 0)
async def post_student(
        email_address: str,
        path_dependency: PathDependency = Depends(sqlalchemy_dependency),
):
    with path_dependency.context.get_context() as context:
        user_repository = UserSqlAlchemyRelationalRepository(context=context)
        filters = {
            "email_address": email_address
        }
        user = UserService.get_user(repository=user_repository, **filters)
        if user is not None:
            return User.parse_obj(user.dict())
