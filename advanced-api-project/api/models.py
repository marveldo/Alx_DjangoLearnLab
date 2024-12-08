from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=120, blank = True , null=True)

    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    title =  models.CharField(max_length=120, blank = True , null=True)
    publication_year = models.IntegerField(blank=True , null=True , default=0)
    author = models.ForeignKey(Author , on_delete=models.CASCADE , blank = True , null=True)
    
    def __str__(self) -> str :
        return str(self.title)