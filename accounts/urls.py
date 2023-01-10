from django.urls import path
from .views import *

urlpatterns = [path('signup/', SignUpView.as_view(), name='signup'),
               path('goal_edit/<int:pk>', EditGoalView.as_view(), name='edit_goal'),
               ]
