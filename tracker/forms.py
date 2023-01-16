from django import forms 
from .models import *


class food_eatenForm(forms.ModelForm):
    
    class Meta:
        model = food_eaten
        fields = "__all__"

    #filtering fooditem selection to user's food items
    def __init__(self, user, *args, **kwargs):
        super(food_eatenForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = fooditem.objects.filter(person=user)
