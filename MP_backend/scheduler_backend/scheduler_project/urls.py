from django.contrib import admin
from django.urls import path, include
from . import views as views1 
from . import models 

urlpatterns = [
    path('', views1.home),
    path('user/', views1.user),
    # path('user/login', views.user_login),
    # path('user/logout', views.user_logout),
    # path('user/signup', views.user_signup),
    path('user/<int:user_id>', views1.user_userid),
    path('process', views1.process),
    path('process/<int:process_id>', views1.process_processid),
    path('schedule/', views1.schedule),
    path('schedule/<int:user_id>', views1.schedule_user),
    path('schedule/<int:user_id>/<int:week>', views1.schedule_user_week),
    path('schedule/<int:user_id>/<int:week>/<int:day>', views1.schedule_user_week_day),
    path('schedule/efficiency/<int:user_id>', views1.schedule_efficiency_user),
    path('schedule/efficiency/<int:user_id>/<int:week>', views1.schedule_efficiency_user_week),
    path('schedule/efficiency/<int:user_id>/<int:week>/<int:day>', views1.schedule_efficiency_user_week_day),
    path('schedule/list_process/<int:user_id>/<int:week>', views1.schedule_listprocess_user_week),
    path('schedule/parameters/<int:user_id>/<int:week>', views1.schedule_parameters_user_week)
]
