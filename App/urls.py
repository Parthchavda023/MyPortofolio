from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
        path('', views.index),
        path('thanks/', views.thanks, name='thanks'),
]
