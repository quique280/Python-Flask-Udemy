class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}."


book = Book("Harry Potter")
book2 = Book("Game of thrones")
book3 = Book("Bad Jokes")

shelf = Bookshelf(book, book2, book3)


print(shelf)