# Generated by Django 3.2.14 on 2022-08-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0004_membership_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]