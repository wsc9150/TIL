from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def sendEmail(request) :
    return HttpResponse('sendEmail')