# Generated by Django 3.2.14 on 2022-08-31 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20220830_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
