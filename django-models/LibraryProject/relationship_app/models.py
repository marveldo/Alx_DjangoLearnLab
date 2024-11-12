from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=150)

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author , blank=True , null=True ,on_delete=models.SET_NULL)

    class Meta :
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=150)
    library = models.OneToOneField(Library , blank=True , null=True , on_delete=models.SET_NULL)

class Rolechoices(models.TextChoices):
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=300, choices=Rolechoices.choices)