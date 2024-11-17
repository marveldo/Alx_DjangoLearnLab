from django.db import models

# Create your models here.
from django.contrib.auth.models import  BaseUserManager , AbstractUser
# Create your models here.


class CustomUsermanager(BaseUserManager):

    def create_user(self, email, password=None , **other_fields) :
        if not email :
            raise ValueError('Email Must be provided')
        user_email = self.normalize_email(email)
        user = self.model(email = user_email , **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None , **other_fields):

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        return self.create_user(email=email, password=password , **other_fields)


class User(AbstractUser):
    date_of_birth = models.DateField(blank = True , null=True)
    profile_photo = models.ImageField(blank = True , null=True , upload_to='images')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUsermanager()
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class Author(models.Model):
    name = models.CharField(max_length=150)

    permissions = [
            ("can_view", "Can View Author"),
            ("can_create", "Can Create author"),
            ("can_edit", "Can Edit author"),
            ("can_delete", "Can Delete author"),
            
        ]
    

    def __str__(self) -> str:
        return self.name
        
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author , blank=True , null=True ,on_delete=models.SET_NULL)

    class Meta :
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    
    def __str__(self) -> str:
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=150)
    library = models.OneToOneField(Library , blank=True , null=True , on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name

class Rolechoices(models.TextChoices):
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'
class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=300, choices=Rolechoices.choices)

    def __str__(self):
        return self.user.username