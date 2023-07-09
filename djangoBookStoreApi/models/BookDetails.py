from django.db import models
from .Books import Books

class BookDetails(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)
    copies_sold = models.IntegerField()
    created_at = models.DateField()
    deleted_at = models.DateField(null=True)

    def __str__(self):
        return self.id
