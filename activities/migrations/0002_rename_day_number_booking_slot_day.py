# Generated by Django 3.2.14 on 2022-09-01 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_slot',
            old_name='day_number',
            new_name='day',
        ),
    ]