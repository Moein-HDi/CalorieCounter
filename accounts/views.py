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


@login_required(login_url='login')
def EditGoalView(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)
        user.calorie_goal = request.POST.get('calorie_goal')
        user.save()
        return redirect('/') #should change to profile
    
    return render(request, 'goal_edit.html')
