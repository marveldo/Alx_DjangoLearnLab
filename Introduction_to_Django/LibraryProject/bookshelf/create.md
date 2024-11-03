>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984",author="George Orwell",publication_year=1949)
>>> print(book)
Book object (1)
>>> print(book.author)
George Orwell
>>> print(book.title)
1984
>>> print(book.id)
1
