from django.db import models
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

