from django.urls import path
from .views import *

urlpatterns = [path('signup/', SignUpView.as_view(), name='signup'),
               path('goal_edit/', EditGoalView, name='edit_goal'),
               ]
