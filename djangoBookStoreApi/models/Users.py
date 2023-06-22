from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateField()
    deleted_at = models.DateField(null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name

# Populating the database with the provided data
#Users.objects.create(name='Bill', created_at='2023-06-06')
#Users.objects.create(name='Jim', created_at='2023-06-07')
#Users.objects.create(name='Phil', created_at='2023-06-08')
#Users.objects.create(name='Kevin', created_at='2023-06-09')
#Users.objects.create(name='Kayle', created_at='2023-06-10')
