from django.contrib import admin
from django.urls import path, include
from sendEmail import views

urlpatterns = [
    path('send/', views.sendEmail),
]
