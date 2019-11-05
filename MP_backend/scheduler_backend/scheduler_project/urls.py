from django.contrib import admin
from django.urls import path, include
from . import views as views1 
from . import models 

urlpatterns = [
    path('', views1.layout)
]
