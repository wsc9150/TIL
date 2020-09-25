from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.



def index(request) :
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()

    context = {'categories' : categories, 'restaurants' : restaurants}

    return render(request, 'index.html', context)


def restaurantDetail(request, res_id) :
    restaurant = Restaurant.objects.get(id = res_id)

    context = {'restaurant' : restaurant}

    return render(request, 'restaurantDetail.html', context)


def restaurantCreate(request) :
    categories = Category.objects.all()

    context = {'categories' : categories}

    return render(request, 'restaurantCreate.html', context)


def categoryCreate(request) :
    categories = Category.objects.all()

    context = {'categories' : categories}

    return render(request, 'categoryCreate.html', context)


def Create_category(request) :
    category_name = request.POST['categoryName']

    new_category = Category(category_name = category_name)
    new_category.save()

    return redirect('index')


def Delete_category(request) :
    category_id = request.POST['categoryId']

    Category.objects.get(id = category_id).delete()

    return redirect('index')


def Create_restaurant(request) :
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)

    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']

    new_res = Restaurant(category = category, restaurant_name = name, restaurant_link = link, restaurant_content = content, restaurant_keyword = keyword)
    new_res.save()

    return redirect('index')


