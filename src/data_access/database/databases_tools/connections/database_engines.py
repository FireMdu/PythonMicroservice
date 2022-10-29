import pyodbc
import functools
import urllib.parse
from getpass import getpass
from urllib.parse import quote_plus as urlquote

import sqlalchemy
import pandas as pd

__all__ = [
    "SQLInteract",
    "SQLLocalPyodbc",
    "SQLAlchemy",
    "MicrosoftSQLServerSQLAlchemy",
    "SQLLocalAlchemy",
    "MySQLServerSQLAlchemy"
]


class SQLInteract:
    def __init__(
            self,
            server,
            database_name,
            server_port=None,
            database_uid="",
            pwd=None,
            driver='{ODBC Driver 17 for SQL Server}',
            conn_obj=pyodbc.connect,
    ):

        self.database_name = database_name
        self.server = server
        self.server_port = server_port
        self.database_uid = database_uid
        self.driver = driver
        self.conn_obj = conn_obj
        self.password = pwd
        if self.server_port is not None:
            self.server = ":".join([self.server, self.server_port])
        self.connection = self.set_connection()

    def set_connection(self):
        return self.conn_obj(self.get_conn_str())

    def get_interpolated_string_secrets(self):
        return f"{self.database_uid}:%s@{self.server}/{self.database_name}" % urlquote(self.password)

    def get_conn_str(self):
        """
        Return the appropriate connection string depending on whether
        the database_uid parameter was specified at the creation of the
        class object.
        """

        if self.database_uid:
            password = self.password or getpass()
            conn_str = f'Driver={self.driver};' \
                       f'Server={self.server};' \
                       f'Database={self.database_name};' \
                       f'UID={self.database_uid};' \
                       f'PWD={password};'
        else:
            conn_str = f'Driver={self.driver};' \
                       f'Server={self.server};' \
                       f'Database={self.database_name};'
        return conn_str

    @functools.lru_cache()
    def read_query(self, query):
        """
        Return a dataframe resulting from the SQL query.
        """

        return pd.read_sql_query(query, self.connection)

    @functools.lru_cache()
    def query_from_dict(self, dictionary, query_key):
        """
        Return dataframe resulting from the SQL query with key 'query_key'
        from a dictionary object where the value of `query_key` is an SQL
        query.
        """

        return self.read_query(dictionary.get(query_key))


class SQLLocalPyodbc(SQLInteract):
    def __init__(
            self,
            *,
            server,
            database_name,
            driver='{SQL Server}',
            conn_obj=pyodbc.connect
    ):
        SQLInteract.__init__(
            self, server, database_name, driver=driver, conn_obj=conn_obj
        )


class SQLAlchemy(SQLInteract):
    def __init__(
            self,
            *,
            server,
            database_name,
            server_port=None,
            database_uid=None,
            pwd="",
            driver='{ODBC Driver 17 for SQL Server}',
            conn_obj=sqlalchemy.create_engine,
    ):
        SQLInteract.__init__(
            self,
            server=server,
            server_port=server_port,
            database_name=database_name,
            database_uid=database_uid,
            driver=driver, conn_obj=conn_obj,
            pwd=pwd,
        )

    def get_conn_str(self):
        if self.database_uid:
            password = self.password
            params = urllib.parse.quote_plus(
                f"Driver={self.driver};Server={self.server};"
                f"Database={self.database_name},"
                f"UID={self.database_uid},PWD={password}"
            )
            conn_str = f"mssql+pyodbc://?odbc_connect={params}"
        else:
            conn_str = "mssql+pyodbc:///?odbc_connect={}".format(
                urllib.parse.quote_plus(
                    "DRIVER={0};SERVER={1};DATABASE={2}".format(
                        self.driver, self.server,
                        self.database_name
                    )
                )
            )
        return conn_str


class MicrosoftSQLServerSQLAlchemy(SQLAlchemy):
    driver = "ODBC Driver 17 for SQL Server"
    
    def set_connection(self):
        return self.conn_obj(
            self.get_conn_str(),
            pool_pre_ping=True,
            pool_size=25, 
            max_overflow=10,
            pool_timeout=60*6
        )

    def get_conn_str(self):
        if self.database_uid:
            conn_str = rf"mssql+pyodbc://{self.get_interpolated_string_secrets()}?driver={self.__class__.driver}"
        else:
            conn_str = "mssql+pyodbc:///?odbc_connect={}".format(
                urllib.parse.quote_plus(
                    "DRIVER={0};SERVER={1};DATABASE={2}".format(
                        self.driver, self.server,
                        self.database_name
                    )
                )
            )
        return conn_str


class MySQLServerSQLAlchemy(SQLAlchemy):
    driver = None

    def set_connection(self):
        return self.conn_obj(
            self.get_conn_str(),
            pool_pre_ping=True,
            pool_size=25,
            max_overflow=10,
            pool_timeout=60 * 6
        )

    def get_conn_str(self):
        if self.database_uid:
            conn_str = rf"mysql://{self.get_interpolated_string_secrets()}"
        else:
            conn_str = "mysql:///?odbc_connect={}".format(
                urllib.parse.quote_plus(
                    "SERVER={0};DATABASE={1}".format(
                        self.server, self.database_name
                    )
                )
            )
        return conn_str


class SQLLocalAlchemy(SQLAlchemy):
    def __init__(
            self, server, database_name,
            driver='{SQL Server}',
            conn_obj=sqlalchemy.create_engine
    ):
        SQLAlchemy.__init__(
            self, server=server, database_name=database_name,
            driver=driver, conn_obj=conn_obj
        )
