# Generated by Django 4.1.5 on 2023-01-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='calorie_goal',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
    ]
