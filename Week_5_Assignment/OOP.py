# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages   # private attribute (encapsulation)

    def get_info(self):
        return f"'{self.title}' by {self.author}, {self.__pages} pages"

    def read(self):
        return f"You start reading '{self.title}'"


# Child class inheriting from Book
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)  # call parent constructor
        self.file_size = file_size

    def get_info(self):
        return f"E-Book: '{self.title}' by {self.author}, File size: {self.file_size}MB"

    def read(self):
        return f"You open '{self.title}' on your e-reader "
    

# Example usage
book1 = Book("1984", "George Orwell", 328)
ebook1 = EBook("Python Basics", "Charles Thuku", 250, 5)

print(book1.get_info())
print(book1.read())

print(ebook1.get_info())
print(ebook1.read())
