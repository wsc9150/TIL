from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.



def index(request) :
    todos = Todo.objects.all()
    context = {'todos' : todos}

    return render(request, 'my_to_do_app/index.html', context)


def createTodo(request) :
    user_input_str = request.POST['todoContent']

    new_todo = Todo(content = user_input_str)
    new_todo.save()

    return redirect('index')


