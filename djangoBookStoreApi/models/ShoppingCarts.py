from django.db import models
from .Users import Users

class ShoppingCarts(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
