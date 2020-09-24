from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('createTodo/', views.createTodo, name = 'createTodo'),
    path('deleteTodo/', views.deleteTodo, name = 'deleteTodo'),
]