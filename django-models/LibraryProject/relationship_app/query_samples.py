from .models import Author , Book , Library
author_name = 'John Doe'
author = Author.objects.get(name = author_name)

authors_books = author.books_set.all()
print(authors_books)
library_name = 'John Does library'
library = Library.objects.get(name = library_name)
libraries_books = library.books.all()
print(library)
print(libraries_books)
librarian = library.librarian
print(librarian)