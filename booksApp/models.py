from django.db import models

class BooksModel(models.Model):
    name = models.CharField(max_length=120)
    status = models.CharField(max_length=120,default="")
    numberOfBook = models.IntegerField()
    def __str__(self):
        return self.name
