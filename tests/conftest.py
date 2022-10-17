from typing import Any, Generator, Type

import pytest
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

import sqlalchemy as sa
from sqlalchemy import event
from src.app_definitions import ROOT_DIR
from src.data_access.database.models.base_entity import InoversityLibraryBase
from src.distribution.api.routers.users_api import PathDependency, sqlalchemy_dependency
from src.data_access.database.databases_tools.contexts.context_types import SqlAlchemyContext
from src.distribution.api.api_manager import App


db_name = "InoversityLibraryModel"
dbEngine = sa.create_engine(f'sqlite:///{ROOT_DIR}/{db_name}.db', echo=True)


@event.listens_for(dbEngine, "connect")
def connect(dbapi_conn, rec):
    dbapi_conn.execute(f'ATTACH DATABASE \'{db_name}.db\' AS \'{db_name}\'')


database_session = sessionmaker(autocommit=False, autoflush=False, bind=dbEngine)

InoversityLibraryBase.metadata.create_all(dbEngine)


def start_application():
    return App().application


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    InoversityLibraryBase.metadata.create_all(dbEngine)
    _app = start_application()
    yield _app
    InoversityLibraryBase.metadata.drop_all(dbEngine)


@pytest.fixture(scope="function")
def client(app: FastAPI) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_database_session` dependency that is injected into routes.
    """

    def sqlalchemy_dependency_override():
        context = SqlAlchemyContext()
        sess = database_session()
        context.sqlalchemy_session, context.context = sess, sess
        yield PathDependency(context=context)

    app.dependency_overrides[sqlalchemy_dependency] = sqlalchemy_dependency_override
    with TestClient(app) as client:
        yield client
