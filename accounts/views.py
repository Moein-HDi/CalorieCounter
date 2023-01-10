from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy 
from django.views import generic
from .models import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'



