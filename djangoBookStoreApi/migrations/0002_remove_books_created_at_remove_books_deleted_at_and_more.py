# Generated by Django 4.2.2 on 2023-07-26 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBookStoreApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='books',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='shoppingcartbooks',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='shoppingcartbooks',
            name='deleted_at',
        ),
    ]
