class Library:
    def __init__(self,name):
        self.name = name
        self.book = []

    def add_book(self,book):
        self.book.append(book)

    def remove_book(self,book):
        self.book.remove(book)

    def print_book(self):
            return[f"{book.title} written by {book.author}" for book in self.book]


class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

library = Library("Big library")
book1 = Book("Harry Potter","J.K. Rowling")
book2 = Book("The Hobbit","J.R.R. Tolkin")
book3 = Book("The Concept Of Physics","H.C Verma")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.print_book())
for book in library.print_book():
    print(book)
