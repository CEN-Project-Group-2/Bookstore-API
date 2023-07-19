from django.db import models
from .Users import Users

class WishLists(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    wishlist_name = models.CharField(max_length=255, unique=True, default='0')

    def __str__(self):
        return self.id
