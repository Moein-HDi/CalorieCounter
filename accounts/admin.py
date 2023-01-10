from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin 
from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import CustomUser

class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm 
    model = CustomUser

    list_display = ['email', 'username', 'calorie_goal', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('calorie_goal',)}),
)

admin.site.register(CustomUser, CustomUserAdmin)