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
    path('process/', views1.process),
    path('process/<int:process_id>', views1.process_processid),
    path('efficiency/<int:user_id>', views1.efficiency_userid),
    path('slots/<int:user_id>', views1.slots_userid)
]
