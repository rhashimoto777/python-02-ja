class Library:
    def __init__(self):
        self._booklist = []

    def add_book(self, title, author):
        book = {"title" : title, "author" : author}
        self._booklist.append(book)
        return
    
    def remove_book(self, title):
        indexes = [i for i, book in enumerate(self._booklist) if book["title"] == title]
        for index in indexes:
            del self._booklist[index]
        return 
    
    def retrieve_books(self):
        return self._booklist
        

my_library = Library()
my_library.add_book("1984", "George Orwell")
my_library.add_book("To Kill a Mockingbird", "Harper Lee")
for book in my_library.retrieve_books():
    print(book)
my_library.remove_book("1984")
for book in my_library.retrieve_books():
    print(book)