# Generated by Django 4.1.5 on 2023-01-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_eaten',
            name='meal',
            field=models.CharField(choices=[('breakfast', 'صبحانه'), ('lunch', 'نهار'), ('dinner', 'شام')], max_length=50),
        ),
    ]