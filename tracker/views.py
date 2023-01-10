from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import *
from accounts.models import CustomUser
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url='login')
def FoodItemListView(request):
    FoodList = fooditem.objects.filter(person=request.user)
    context = {
        'FoodList': FoodList,
    }
    return render(request, 'fooditem_list.html', context)


class FoodItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = fooditem
    template_name = 'fooditem_new.html'
    fields = "__all__"
    success_url = reverse_lazy('fooditem_list')

class FoodItemDeleteView(LoginRequiredMixin ,generic.DeleteView): 
    model = fooditem 
    template_name = 'fooditem_delete.html' 
    success_url = reverse_lazy('fooditem_list')



