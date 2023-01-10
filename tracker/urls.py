from django.urls import path
from .views import FoodItemCreateView, FoodItemListView, FoodItemDeleteView, FoodEatenCreateView, FoodEatenDeleteView, ProfileView, EditGoalView

urlpatterns = [
    path('fooditem_new/', FoodItemCreateView.as_view(), name='fooditem_new'),
    path('fooditem_list/', FoodItemListView, name='fooditem_list'),
    path('fooditem_delete/<int:pk>', FoodItemDeleteView.as_view(), name='fooditem_delete'),
    path('foodeaten_new/', FoodEatenCreateView, name='foodeaten_new'),
    path('foodeaten_delete/<int:pk>', FoodEatenDeleteView.as_view(), name='foodeaten_delete'),
    path('profile/', ProfileView, name='profile'),
    path('goal_edit/', EditGoalView, name='goal_edit'),
    
]
