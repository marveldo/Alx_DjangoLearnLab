from .models import Author , Book , Library

author = Author.objects.get(name = 'John Doe')

authors_books = author.books_set.all()
print(authors_books)

library = Library.objects.get(name = 'John Does library')
libraries_books = library.books.all()
print(library)
print(libraries_books)
librarian = library.librarian
print(librarian)