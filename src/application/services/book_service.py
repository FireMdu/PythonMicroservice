from src.application.models.book import Book

class BookService:

    def get_all_books(self):
        print('Simulating getting books')
        return [Book("The Goal"), Book("Five Dysfunctions")]
    
    def get_book(self, id):
        print('Simulating getting specific book')
        return Book("The Goal", id)