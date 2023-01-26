from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('checkup', views.checkup, name = 'Checkup'),
    path('checkup/result', views.prediction, name = 'Prediction')
]
