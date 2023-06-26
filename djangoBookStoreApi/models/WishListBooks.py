from django.db import models
from .WishLists import WishLists
from .Books import Books

class WishListBooks(models.Model):
    id = models.AutoField(primary_key=True)
    wish_list = models.ForeignKey(WishLists, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    created_at = models.DateField()
    deleted_at = models.DateField(null=True)

    def __str__(self):
        return self.id
