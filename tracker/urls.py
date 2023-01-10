from django.urls import path
from .views import FoodItemCreateView, FoodItemListView, FoodItemDeleteView

urlpatterns = [
    path('fooditem_new/', FoodItemCreateView.as_view(), name='fooditem_new'),
    path('fooditem_list/', FoodItemListView, name='fooditem_list'),
    path('fooditem_delete/<int:pk>', FoodItemDeleteView.as_view(), name='fooditem_delete'),
    
]
