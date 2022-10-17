from src.application.models.library_management.document import Document


_all__ = [
    "DocumentService"
]


class DocumentService:

    @staticmethod
    def get_all_books():
        print('Simulating getting documents')
        return [Document(), Document()]

    @staticmethod
    def get_document(**kwargs):
        print('Simulating getting specific document')
        return Document(**kwargs)
