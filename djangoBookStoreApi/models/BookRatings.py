from django.db import models
from .Users import Users
from .Books import Books

class BookRatings(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    score = models.SmallIntegerField()

    def __str__(self):
        return str(self.id)
    
