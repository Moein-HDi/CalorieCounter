from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import *
from accounts.models import CustomUser
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date


@login_required(login_url='login')
def FoodItemListView(request):
    FoodList = fooditem.objects.filter(person=request.user)
    if FoodList.count() == 0:
        f1 = fooditem(name='مغز بادام (100 گرم)',
                      calorie=575, person=request.user)
        f1.save()
        f1 = fooditem(name='برنج پخته آبکش (یک کفگیر)',
                      calorie=238, person=request.user)
        f1.save()
        f1 = fooditem(name='بیسکوییت ساقه طلایی (1 عدد)',
                      calorie=55, person=request.user)
        f1.save()
        f1 = fooditem(name='تخم مرغ آب پز (یک عدد)',
                      calorie=78, person=request.user)
        f1.save()
        f1 = fooditem(name='خرما (یک عدد)', calorie=20, person=request.user)
        f1.save()
        f1 = fooditem(name='سیب (یک عدد)', calorie=80, person=request.user)
        f1.save()
        f1 = fooditem(name='کیک شکلاتی (100 گرم)',
                      calorie=466, person=request.user)
        f1.save()
        f1 = fooditem(name='نان جو (100 گرم)',
                      calorie=250, person=request.user)
        f1.save()
        f1 = fooditem(name='گوشت قرمز (100 گرم)',
                      calorie=250, person=request.user)
        f1.save()
        f1 = fooditem(name='گوشت مرغ (100 گرم)',
                      calorie=200, person=request.user)
        f1.save()
        return redirect('/manage/fooditem_list')

    context = {
        'FoodList': FoodList,
    }
    return render(request, 'fooditem_list.html', context)


class FoodItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = fooditem
    template_name = 'fooditem_new.html'
    fields = "__all__"
    success_url = reverse_lazy('fooditem_list')


class FoodItemDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = fooditem
    template_name = 'fooditem_delete.html'
    success_url = reverse_lazy('fooditem_list')


def ProfileView(request):
    # user = CustomUser.objects.get(id=request.user.id)
    # user_goal = user.calorie_goal
    # user_consumed_today =
    UserFoodEatenList = food_eaten.objects.filter(person=request.user)
    TodayFoodEatenList = UserFoodEatenList.filter(date=date.today())

    context = {
        'FoodEatenList': TodayFoodEatenList,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def FoodEatenCreateView(request):
    userperson = CustomUser.objects.get(id=request.user.id)
    form = food_eatenForm(request.user, instance=userperson)

    if request.method == "POST":
        form = food_eatenForm(request.user, request.POST, instance=userperson)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            meal = form.cleaned_data.get('meal')
            person = form.cleaned_data.get('person')
            eatfood = food_eaten.objects.create(name=name, meal=meal, person=person)
            eatfood.save()
            return redirect('/manage/profile')
        else:
            form = food_eatenForm(request.user)
    context = {'form': form}
    return render(request, 'foodeaten_new.html', context)


class FoodEatenDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = food_eaten
    template_name = 'foodeaten_delete.html'
    success_url = reverse_lazy('profile')
