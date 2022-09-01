# Generated by Django 3.2.14 on 2022-09-01 19:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_rename_day_number_booking_slot_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_slot',
            name='day',
            field=models.PositiveSmallIntegerField(choices=[(1, 'monday'), (2, 'tuesday'), (3, 'wednesday'), (4, 'thursday'), (5, 'friday'), (6, 'saturday'), (7, 'sunday')], validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(1)]),
        ),
    ]