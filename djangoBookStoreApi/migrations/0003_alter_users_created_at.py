# Generated by Django 4.2.2 on 2023-07-07 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBookStoreApi', '0002_users_email_users_home_address_users_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]