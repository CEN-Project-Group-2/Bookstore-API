from django.db import models
from .Users import Users
from .Books import Books

class BookComments(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.id
