# Generated by Django 4.1.5 on 2023-01-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_food_eaten_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_eaten',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
