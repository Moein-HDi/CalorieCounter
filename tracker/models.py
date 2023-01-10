from django.db import models
from accounts.models import CustomUser


class fooditem(models.Model):
    name = models.CharField(max_length=200)
    calorie = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, blank=True)
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    

    def __str__(self):
        return str('{name} ({cal} کالری)'.format(name=self.name, cal=self.calorie))


class food_eaten(models.Model):
    meals = (
        ('breakfast', 'صبحانه'),
        ('lunch', 'نهار'),
        ('dinner', 'شام'),
    )
    name = models.ManyToManyField(fooditem)
    date = models.DateField(auto_now_add=True)
    meal = models.CharField(max_length=50, choices=meals)
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
