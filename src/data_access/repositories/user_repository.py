import itertools as it
from typing import Optional, List, Union

from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound

from src.data_access.database.models.users import UserEntity
from src.data_access.database.models.user_type_entity import UserTypeEntity
from src.common.models.library_management. user import user_types as enum_typ
from src.common.models.library_management.user import User, UserInDatabase, UserType
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase

__all__ = [
    "UserSqlAlchemyRelationalRepository"
]


NO_IMPLEMENTATION = "No implementation"


class UserSqlAlchemyRelationalRepository(SqlAlchemyRelationalRepositoryBase):
    def __init__(self, context: Session) -> None:
        super().__init__(context=context)

    def add(self, *args, **kwargs) -> User:
        raise NotImplementedError("Must be implemented by the repository subclass.")

    def _add_user(self, *, user_type: Union[enum_typ.UserTypes, str], user: User) -> User:
        user_type_entity = UserTypeEntity(**UserType(user_type=user_type).dict())
        user_model: UserInDatabase = UserInDatabase.parse_obj(user.dict())
        db_user_type_query = self.context.query(UserTypeEntity)
        db_user_type_entity = db_user_type_query.filter(UserTypeEntity.user_type == user_type_entity.user_type).first()
        if db_user_type_entity is not None:
            user_type_entity = db_user_type_entity

        db_user = self.context.query(UserEntity)
        try:
            db_user = db_user.filter(UserEntity.email_address == user_model.email_address).scalar()
        except MultipleResultsFound:
            return UserInDatabase.from_orm(db_user.first())

        if db_user is not None:
            return UserInDatabase.from_orm(db_user)

        user_entity = UserEntity(user_type_entity=user_type_entity, **user_model.dict())
        self.context.add(user_entity)
        self.sync()
        return UserInDatabase.from_orm(user_entity)

    def list(self, *user_types: Union[enum_typ.UserTypes, str]) -> List[User]:
        return self._list_users(*user_types)

    def _list_users(self, *user_types: Union[enum_typ.UserTypes, str]) -> List[User]:
        db_user_type_query = self.context.query(UserTypeEntity)
        db_user_type = db_user_type_query.where(UserTypeEntity.user_type.in_(list(user_types))).all()
        if db_user_type is None:
            return []
        user_groups = (ele.user_entity for ele in db_user_type)
        return [User.from_orm(ele) for ele in it.chain.from_iterable(user_groups)]

    def get(self, **filters) -> Optional[User]:
        db_user = self.context.query(UserEntity).filter_by(**filters).first()
        if db_user is not None:
            return User.from_orm(db_user)

    def update(self, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def delete(self, id_):
        raise NotImplementedError(NO_IMPLEMENTATION)
