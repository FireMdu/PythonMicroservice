import contextlib
from typing import TypeVar
from abc import ABC, abstractmethod

__all__ = [
    "ServiceContext"
]


Context = TypeVar("Context")


class ServiceContext(ABC):

    def __init__(self, context: Context) -> None:
        self.context = context

    @contextlib.contextmanager
    def get_context(self):
        try:
            yield self.context
            self.commit()
        except BaseException as err:
            self.rollback()
            raise err
        finally:
            self.close()

    @abstractmethod
    def close(self) -> None: ...

    @abstractmethod
    def commit(self) -> None: ...

    @abstractmethod
    def rollback(self) -> None: ...
