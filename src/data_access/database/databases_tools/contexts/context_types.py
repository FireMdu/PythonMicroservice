from sqlalchemy.orm import Session

from src.data_access.context import ServiceContext
from src.data_access.database.databases_tools.contexts.connection_context import relational_database_context

__all__ = [
    "SqlAlchemyContext"
]


class SqlAlchemyContext(ServiceContext):

    def __init__(self) -> None:
        self.sqlalchemy_session: Session = relational_database_context()
        super().__init__(context=self.sqlalchemy_session)

    def close(self) -> None:
        self.context.close()

    def commit(self) -> None:
        self.context.commit()

    def rollback(self) -> None:
        self.context.rollback()
