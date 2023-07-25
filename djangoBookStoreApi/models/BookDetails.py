from django.db import models
from .Books import Books

class BookDetails(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    year = models.IntegerField()
    copies_sold = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.ISBN}"
