from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField(null=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    home_address = models.CharField(max_length=255, null=True, blank=True)

    last_login = None

    def __str__(self):
        return str(self.id)
    
