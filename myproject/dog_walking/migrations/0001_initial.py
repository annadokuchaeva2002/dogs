# Generated by Django 5.1.1 on 2024-09-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strolls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_number', models.IntegerField()),
                ('animal_name', models.CharField(max_length=50)),
                ('day', models.DateField()),
                ('time_in_day', models.CharField(max_length=50)),
            ],
        ),
    ]
