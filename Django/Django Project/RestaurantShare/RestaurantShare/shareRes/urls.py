from django.contrib import admin
from django.urls import path, include
from shareRes import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurantDetail/delete', views.Delete_restaurant, name = 'resDelete'),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name = 'resDetailPage'),
    path('restaurantDetail/updatePage/update', views.Update_restaurant, name = 'resUpdate'),    # 아래 url 보다 위에 있어야 한다. 순서 중요
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name = 'resUpdatePage'),
    path('restaurantCreate/', views.restaurantCreate, name = 'resCreatePage'),
    path('categoryCreate/', views.categoryCreate, name = 'cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name = 'cateCreate'),
    path('categoryCreate/delete', views.Delete_category, name = 'cateDelete'),
    path('restaurantCreate/create', views.Create_restaurant, name = 'resCreate'),
]
