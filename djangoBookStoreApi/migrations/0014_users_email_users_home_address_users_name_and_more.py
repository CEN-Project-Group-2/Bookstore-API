# Generated by Django 4.2.2 on 2023-07-07 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBookStoreApi', '0013_remove_users_email_remove_users_home_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='home_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, default='default-username', max_length=255, null=True),
        ),
    ]