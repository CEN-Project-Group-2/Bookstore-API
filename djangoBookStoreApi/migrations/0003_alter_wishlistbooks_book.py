# Generated by Django 4.2.2 on 2023-07-04 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBookStoreApi', '0002_alter_wishlistbooks_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlistbooks',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoBookStoreApi.books'),
        ),
    ]
