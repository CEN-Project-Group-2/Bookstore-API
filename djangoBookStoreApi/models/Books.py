from django.db import models

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateField()
    deleted_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.id