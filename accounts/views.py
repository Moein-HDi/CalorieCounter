from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy 
from django.views import generic
from .models import CustomUser


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'

class EditGoalView(generic.UpdateView):
    model = CustomUser #wtf
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home') #should change later
    template_name = 'goal_edit.html'
