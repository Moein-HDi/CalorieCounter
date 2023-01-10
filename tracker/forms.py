from django import forms 
from .models import *

class fooditemForm(forms.ModelForm):
    
    class Meta:
        model = fooditem
        fields = ['name', 'calorie']        

    #filtering food item selection to user's food items 
    def __init__(self, user, *args, **kwargs):
        super(fooditemForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = fooditem.objects.filter(person=user)


class food_eatenForm(forms.ModelForm):
    
    class Meta:
        model = food_eaten
        fields = ['name', 'meal']

    #filtering fooditem selection to user's food items
    def __init__(self, user, *args, **kwargs):
        super(fooditemForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = fooditem.objects.filter(person=user)
