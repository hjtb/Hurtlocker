# Generated by Django 3.2.14 on 2022-09-05 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0012_auto_20220904_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_slot',
            name='day',
            field=models.IntegerField(choices=[(0, 'Mon'), (1, 'Tue'), (2, 'Wed'), (3, 'Thur'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')], validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(1)]),
        ),
    ]