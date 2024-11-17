>>>from bookshelf.models import Book
>>> get_book = Book.objects.get(title="1984")
>>> get_book.delete()
(1, {'bookshelf.Book': 1})