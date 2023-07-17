from django.db import models
from .ShoppingCarts import ShoppingCarts
from .Books import Books

class ShoppingCartBooks(models.Model):
    id = models.AutoField(primary_key=True)
    shopping_cart = models.ForeignKey(ShoppingCarts, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField(null=True)

    def __str__(self):
        return self.id
