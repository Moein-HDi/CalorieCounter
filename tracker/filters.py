import django_filters
from .models import *
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class fooditemFilter(django_filters.FilterSet):
    date = django_filters.CharFilter(widget=AdminJalaliDateWidget())
    class Meta:
        model = food_eaten
        fields = ['date']
    
    