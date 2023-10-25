from django.shortcuts import render,redirect
from django.http import HttpResponse
from toDoList.models import TodoList
from toDoList.form import ToDoForm
from django.contrib import messages
import sys

# Create your views here.
# def toDoList(request):
#     return HttpResponse('Your To Do\'s are Here, Glad to Have you here!')

def toDoList(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('ToDo\'s added successfully!'))
        return redirect('toDoList')
    else:
        datas = {'welcome_text': 'Warm Welcome from To Do Page!', 'data':TodoList.objects.all} # get all objects from model to view, import which to retrieve data with use of objects.all method, this method return data as List datatype
        return render(request,'todo.html',datas)

def editToDo(request,todo_id):
    if request.method == 'POST':
        todo = TodoList.objects.get(pk=todo_id)
        form = ToDoForm(request.POST or None, instance=todo) # this instance will find the requested edit object in db through models
        if form.is_valid():
            form.save()
            messages.success(request,('ToDo Updated Successfully!'))
            return redirect('toDoList')
    else:
        todo_obj = TodoList.objects.get(pk=todo_id)
        datas = {'data':todo_obj}
        return render(request,'editToDo.html',datas)

def deleteToDo(request,todo_id):
    selectToDo = TodoList.objects.get(pk=todo_id)
    if selectToDo.delete():
        messages.success(request,('ToDo deleted Successfully!'))
        return redirect('toDoList')
    

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