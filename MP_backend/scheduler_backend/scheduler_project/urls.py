from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from . import views as views1 
from . import models 
from rest_framework.authtoken import views as viewsauth

urlpatterns = [
    path('', views1.home),
    path('user/', views1.user),
    path('api/user/', views1.api_user),
    path('user/logout',views.LogoutView.as_view(), name='logout'),
    path('user/signup/',views1.user_signup),
    path('api/user/signup/',views1.api_user_signup), 
    path('user/login/', views.LoginView.as_view(), name='login'),
    path('api/user/login/', views1.api_user_login),

    # path('api-token-auth/', viewsauth.obtain_auth_token, name = 'api_token_auth'),

    # path('user/signup', views.user_signup),
    path('user/<int:user_id>', views1.user_userid),
    path('api/user/<int:user_id>', views1.api_user_userid), 
    path('process/<int:user_id>', views1.process_userid),
    path('api/process/<int:user_id>', views1.api_process_userid), 
    path('process/<int:user_id>/<int:process_id>', views1.process_userid_processid),
    path('api/process/<int:user_id>/<int:process_id>', views1.api_process_userid_processid),
    path('efficiency/<int:user_id>', views1.efficiency_userid),
    path('api/efficiency/<int:user_id>', views1.api_efficiency_userid),
    path('slots/<int:user_id>', views1.slots_userid),
    path('api/slots/<int:user_id>', views1.api_slots_userid),
    path('parameters/<int:user_id>', views1.parameters_userid),
    path('api/parameters/<int:user_id>', views1.api_parameters_userid),
    # path('fullscreen/', views1.fullscreen)
    path('schedule/<int:user_id>/', views1.schedule_userid),
    # path('api/userid', views1.api_userid)
]
