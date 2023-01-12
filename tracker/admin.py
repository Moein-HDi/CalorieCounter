from django.contrib import admin
from .models import *
# Register your models here.

class fooditemAdmin(admin.ModelAdmin):
    list_display = ('person', 'name', 'calorie')

class food_eatenAdmin(admin.ModelAdmin):
    list_display = ('person', 'name', 'meal', 'date')


admin.site.register(fooditem, fooditemAdmin)
admin.site.register(food_eaten, food_eatenAdmin)