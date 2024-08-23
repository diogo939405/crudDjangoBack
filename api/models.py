from django.db import models

class Book(models.Model):
    bookTitle = models.CharField(max_length=50)
    Lancamento = models.IntegerField()
    
    def __str__(self) -> str:
        return self.bookTitle