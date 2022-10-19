from abc import ABC
from typing import Optional

from src.data_access.repositories.base_repository import RepositoryBase

__all__ = [
    "AbstractDomainService"
]


class AbstractDomainService(ABC):
    repository: Optional[RepositoryBase] = None

    def __init__(self, context) -> None:
        self.context = context
