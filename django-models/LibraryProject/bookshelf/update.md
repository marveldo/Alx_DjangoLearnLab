>>> get_book = Book.objects.get(title="1984")
>>> get_book.title = "Nineteen Eighty-Four"
>>> get_book.save()
>>>