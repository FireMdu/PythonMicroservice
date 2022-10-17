from typing import List

from src.common.models.library_management.document import Document
from src.application.abstract_domain_service import AbstractDomainService


_all__ = [
    "DocumentService"
]


class DocumentService(AbstractDomainService):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_all_books(*args, **kwargs) -> List[Document]:
        print('Simulating getting documents')
        return [Document(**kwargs), Document(**kwargs)]

    @staticmethod
    def get_document(*args, **kwargs) -> Document:
        print('Simulating getting specific document')
        return Document(**kwargs)
