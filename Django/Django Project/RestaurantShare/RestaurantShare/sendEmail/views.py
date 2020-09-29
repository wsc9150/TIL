from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def sendEmail(request) :
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    print(checked_res_list, "/", inputReceiver, "/", inputTitle, "/", inputContent)

    return redirect('index')


