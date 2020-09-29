from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

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


def restaurantUpdate(request, res_id) :
    print('res_id : ', res_id)
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id)
    # print('----', categories[0])
    # print('----', restaurant.category)

    context = {'categories' : categories, 'restaurant' : restaurant}

    return render(request, 'restaurantUpdate.html', context)


def Update_restaurant(request) :
    print('aaaaaaa')
    resId = request.POST['resId']
    print('resId : ', resId)

    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id = change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']

    before_restaurant = Restaurant.objects.get(id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()

    return HttpResponseRedirect(reverse('resDetailPage', kwargs = {'res_id' : resId}))  # kwargs 를 쓸땐 단순히 redirect가 안된다. HttpResponseRedirect 사용


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


def Delete_restaurant(request) :
    res_id = request.POST['resId']

    restaurant = Restaurant.objects.get(id = res_id)
    restaurant.delete()

    return redirect('index')


