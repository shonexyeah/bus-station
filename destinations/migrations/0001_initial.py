# Generated by Django 4.0.6 on 2022-07-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('address_street', models.CharField(max_length=128)),
                ('address_city', models.CharField(max_length=64)),
                ('address_zip', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]