from django.db import models
from .Users import Users

class Books(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE) 
    created_at = models.DateField()
    deleted_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
