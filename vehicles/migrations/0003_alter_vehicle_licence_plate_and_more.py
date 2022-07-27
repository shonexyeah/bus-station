# Generated by Django 4.0.6 on 2022-07-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_alter_vehicle_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='licence_plate',
            field=models.CharField(max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='seating_capacity',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='unique_number',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]
