# Generated by Django 4.0.6 on 2022-07-28 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_alter_vehicle_options_vehicle_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='licence_plate',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.MinLengthValidator(7)]),
        ),
    ]