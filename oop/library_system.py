#!/bin/bash
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
        def __init__(self, title, author, file_size):
             super().__init__(title, author)
             self.file_size = file_size

class PrintBook(Book):
     def __init__(self, title, author, page_count):
          super().__init__(title, author)
          self.page_count = page_count

class Library:
     def __init__(self):
          self.books = []

     def add_book(self, book):
          self.books.append(book)

     def list_books(self):
          for book in self.books:
               print(book)
          else:
               print("The list is empty")


#my_library = Library()

#classic_book = Book("Pride and Prejudice", "Jane Austen")
#digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
#paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

#my_library.add_book(classic_book)
