# Generated by Django 3.1 on 2020-03-16 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
    ]
