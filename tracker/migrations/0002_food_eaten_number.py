# Generated by Django 4.1.5 on 2023-01-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_eaten',
            name='number',
            field=models.IntegerField(default=1, max_length=5),
        ),
    ]
