from typing import Optional

__all__ = [
    "DocumentOutOfOrder",
    "InvalidUserIdentifier"
]


class DocumentOutOfOrder(Exception):

    def __init__(self, document_title: str, message: str = None) -> None:
        self.message = message
        self.document_title = document_title
        if not message:
            self.message = f"The requested document titled: {self.document_title} is out of order"
        super().__init__(self.message)


class InvalidUserIdentifier(Exception):
    def __init__(self, user_identifier: Optional[str], message: str = None) -> None:
        self.message = message
        self.user_identifier = user_identifier
        if not message:
            self.message = f"Invalid user identifier: {self.user_identifier}"
        super().__init__(self.message)
