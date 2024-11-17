from .models import Author , Book , Library , Librarian
author_name = 'John Doe'
author = Author.objects.get(name=author_name)

authors_books = Book.objects.filter(author=author)
print(authors_books)
library_name = 'John Does library'
library = Library.objects.get(name=library_name)
libraries_books =   library.books.all()
print(library)
print(libraries_books)
librarian = Librarian.objects.get(library=library)
print(librarian)