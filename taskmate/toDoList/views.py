from django.shortcuts import render
from django.http import HttpResponse
from toDoList.models import TodoList
import sys

# Create your views here.
# def toDoList(request):
#     return HttpResponse('Your To Do\'s are Here, Glad to Have you here!')

def toDoList(request):
    datas = {'welcome_text': 'Warm Welcome from To Do Page!', 'data':TodoList.objects.all} # get all objects from model to view, import which to retrieve data with use of objects.all method, this method return data as List datatype
    return render(request,'todo.html',datas)

def taskList(request):
    datas = {'data':'Warm Welcome from Task Page!'}
    return render(request,'task.html',datas)
    # here for the render () it accepts three parameters 1st - request from browser from clientside, 2nd - which html template should render, 3rd - dynamic datas remember it always a form of dictionaries
    
def contactList(request):
    datas = {'data': 'Warm Welcome from Contact Page!'}
    return render(request,'contact.html',datas)

def aboutUs(request):
    datas = {'data': 'Warm Welcome from About Page!'}
    return render(request,'about.html',datas)