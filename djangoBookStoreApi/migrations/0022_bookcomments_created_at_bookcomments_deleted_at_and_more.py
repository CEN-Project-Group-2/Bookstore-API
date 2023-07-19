# Generated by Django 4.2.2 on 2023-07-12 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBookStoreApi', '0021_merge_20230711_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcomments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bookcomments',
            name='deleted_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='shoppingcartbooks',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]