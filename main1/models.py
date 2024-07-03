from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    

