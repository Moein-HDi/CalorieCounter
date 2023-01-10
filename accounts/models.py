from django.contrib.auth.models import AbstractUser 
from django.db import models

class CustomUser(AbstractUser): 
    calorie_goal = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=2000.00)