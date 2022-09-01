# Generated by Django 3.2.14 on 2022-09-01 19:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=255, unique=True)),
                ('booking_slot_limit', models.IntegerField(default=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Booking_Slot',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('day_number', models.PositiveSmallIntegerField(choices=[('1', 'monday'), ('2', 'tuesday'), ('3', 'wednesday'), ('4', 'thursday'), ('5', 'friday'), ('6', 'saturday'), ('7', 'sunday')], validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(1)])),
                ('start_hour', models.TimeField()),
                ('duration', models.DurationField(max_length=255, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.activity', to_field='activity_name')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('booking_slot_used', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities.booking_slot')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile', to_field='user')),
            ],
        ),
    ]
