# Generated by Django 4.2.2 on 2023-07-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBookStoreApi', '0004_wishlists_wishlist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlists',
            name='wishlist_name',
            field=models.CharField(default='0', max_length=255, unique=True),
        ),
    ]
