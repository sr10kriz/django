from django.shortcuts import render,redirect
from django.http import HttpResponse
from toDoList.models import TodoList
from toDoList.form import ToDoForm
from django.contrib import messages
from django.core.paginator import Paginator
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
        toDos = TodoList.objects.all() # if we use pagination then u must mention objects.all with paranthesis like this object.all() else we got error, if we dont use pagination then dont need to be mention paranthesis
        paginationIns = Paginator(toDos,5) # this paginator class accepts two arguments, 1 is which datas to paginate, 2 is page limit 
        whichPage = request.GET.get('page') # here we create url parameters using pagination instance that we created on above line
        toDos = paginationIns.get_page(whichPage)
        datas = {'welcome_text': 'Warm Welcome from To Do Page!', 'data':toDos} # get all objects from model to view, import which to retrieve data with use of objects.all method, this method return data as List datatype
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
    
def completeToDo(request,todo_id):
    toDo = TodoList.objects.get(pk=todo_id)
    if toDo.status == True:
        toDo.status = False
    else:
        toDo.status = True
    toDo.save()
    messages.success(request,('ToDo Marked as per your Wish!'))
    return redirect('toDoList')

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