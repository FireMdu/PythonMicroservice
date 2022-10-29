from typing import TypeVar, List, Optional

from fastapi import APIRouter, Depends
from fastapi_versioning import version

from src.data_access.database import SqlAlchemyContext
from src.distribution.api.schemas import PathDependency
from src.common.models.library_management.account import Account
from src.common.models.library_management.user import User, CreateUser
from src.data_access.repositories.base_repository import RepositoryBase
from src.application.services.library_management import UserService, StudentService, StaffService, AccountService

Repository = TypeVar("Repository", bound=RepositoryBase)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
)


def sqlalchemy_dependency():
    # TODO: Re-look at this dependency creation
    yield PathDependency(context=SqlAlchemyContext())


@router.get("/all", status_code=200, name="Get all users", response_model=List[User])
@version(1, 0)
async def get_all_users(path_dependency: PathDependency = Depends(sqlalchemy_dependency)):
    with path_dependency.context.get_context() as context:
        service = UserService(context=context)
        return service.get_all_users()


@router.post("/student", name="Post student user", status_code=200, response_model=User)
@version(1, 0)
async def post_student(
        student: CreateUser,
        path_dependency: PathDependency = Depends(sqlalchemy_dependency)
):
    with path_dependency.context.get_context() as context:
        service = StudentService(context=context)
        student_user = service.post_a_student_user(student=student)
        return User.parse_obj(student_user.dict())


@router.post("/staff", name="Post staff user", status_code=200, response_model=User)
@version(1, 0)
async def post_staff(
        staff: CreateUser,
        path_dependency: PathDependency = Depends(sqlalchemy_dependency)
):
    with path_dependency.context.get_context() as context:
        service = StaffService(context=context)
        staff = service.post_a_staff_user(staff=staff)
        return User.parse_obj(staff.dict())


@router.get(
    "/{email_address}",
    name="Get user by email address",
    status_code=200,
    response_model=Optional[User]
)
@version(1, 0)
async def get_user_by_email_address(
        email_address: str,
        path_dependency: PathDependency = Depends(sqlalchemy_dependency),
):
    with path_dependency.context.get_context() as context:
        filters = {
            "email_address": email_address
        }
        service = UserService(context=context)
        user = service.get_user_by_filters(**filters)
        if user is not None:
            return User.parse_obj(user.dict())


@router.post(
    "/account/{email_address}",
    name="Create user account by email address",
    status_code=200,
    response_model=Optional[Account]
)
@version(1, 0)
async def create_user_account(
        email_address: str,
        path_dependency: PathDependency = Depends(sqlalchemy_dependency),
):
    with path_dependency.context.get_context() as context:
        service = AccountService(context=context)
        account = service.create_account_for_user(user_email_address=email_address)
        return Account.parse_obj(account.dict())


@router.get(
    "/account/all",
    name="Get all user accounts",
    status_code=200,
    response_model=List[Account]
)
@version(1, 0)
async def get_all_user_account(path_dependency: PathDependency = Depends(sqlalchemy_dependency)):
    with path_dependency.context.get_context() as context:
        service = AccountService(context=context)
        return service.get_all_accounts()
