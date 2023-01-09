from django.db import models
from django.contrib.auth.models import User

# class Person(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     calorie_goal = models.DecimalField(max_digits=5, decimal_places=2, default=2000.00)

#     def __str__(self):
#         return str(self.user.username)

class fooditem(models.Model):
    name = models.CharField(max_length=200)
    calorie = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name + ' (' + self.calorie + ' cal)')

class food_eaten(models.Model):
    meals=(
        ('breakfast','breakfast'),
        ('lunch','lunch'),
        ('dinner','dinner'),
    )
    name = models.ManyToManyField(fooditem)
    date = models.DateField(auto_now_add=True)
    meal = models.CharField(max_length=50, choices=meals)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)



    
