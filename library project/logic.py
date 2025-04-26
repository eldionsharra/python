class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author} | {self.genre} | {self.pages}"

library = []

def add_book(book):
    library.append(book)

def save_library(filename="library.txt"):
    with open(filename, "w") as file:
        for book in library:
            file.write(f"{book.title}, {book.author}, {book.genre}, {book.pages}\n")
