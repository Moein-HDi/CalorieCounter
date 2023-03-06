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
from datetime import timedelta
from .filters import *


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


@login_required(login_url='login')
def ProfileView(request):
    current_user = CustomUser.objects.get(id=request.user.id)
    user_goal = current_user.calorie_goal

    UserFoodEatenList = food_eaten.objects.filter(person=request.user)
    TodayFoodEatenList = UserFoodEatenList.filter(date=date.today())
    YesterdayFoodEatenList = UserFoodEatenList.filter(date=(date.today()-timedelta(days=1)))
    
    total_cal_alltime = 0
    total_cal_today = 0
    total_cal_yesterday = 0
    for food in UserFoodEatenList:
        total_cal_alltime+= (food.name.calorie * food.number)
    for food in TodayFoodEatenList:
        total_cal_today += (food.name.calorie * food.number)
    for food in YesterdayFoodEatenList:
        total_cal_yesterday += (food.name.calorie * food.number)
    

    cal_compared = int(total_cal_today - total_cal_yesterday)
    if cal_compared > 0:
        cal_compared_to_yesterday = "+%d" %cal_compared
    else:
        cal_compared_to_yesterday = cal_compared
    
    goal_percent = int(total_cal_today/user_goal*100)
    context = {
        'FoodEatenList': TodayFoodEatenList,
        'user_goal': int(user_goal),
        'total_cal_today': int(total_cal_today),
        'goal_percent': goal_percent,
        'cal_compared': cal_compared_to_yesterday,
        'cal_alltime': int(total_cal_alltime),
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
            number = form.cleaned_data.get('number')
            person = form.cleaned_data.get('person')
            eatfood = food_eaten.objects.create(
                name=name, number=number, meal=meal, person=person)
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


@login_required(login_url='login')
def EditGoalView(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)
        user.calorie_goal = request.POST.get('calorie_goal')
        user.save()
        return redirect('/manage/profile')

    return render(request, 'goal_edit.html')


@login_required(login_url='login')
def FoodHistoryView(request):
    UserFoodEatenList = food_eaten.objects.filter(person=request.user)
    f = fooditemFilter(request.GET, queryset=UserFoodEatenList)
    return render(request, 'foodhistory.html', {'filter': f})