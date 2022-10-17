from typing import Optional

from pydantic import BaseModel

__all__ = [
    "Document"
]


class Document(BaseModel):
    document_id: Optional[str]
    document_title: Optional[str]
    document_standard_identifier: Optional[str]
