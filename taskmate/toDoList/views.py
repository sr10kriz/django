from django.shortcuts import render, redirect
from django.http import HttpResponse
from toDoList.models import TodoList
from toDoList.form import ToDoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import sys

# Create your views here.
# def toDoList(request):
#     return HttpResponse('Your To Do\'s are Here, Glad to Have you here!')


@login_required  # this how we use the login_required decorator which defaultly comes with django for authentication purpose,
# 1 which views requires this authenticated users only able to see the list/datas need to use login_required decorator
# 2 use @at the rate of login_required then the this view toDoList view accessible only for the authenticated users
# 3 after first two points, we need to redirects users who are not authenticated to a new different location, for this we need mention default LOGIN_URL in settings.py in the root app to our desired location
# 4 if we dont mention the LOGIN_URL in settings.py then we gonna get default error that comes under django


def toDoList(request):
    if request.method == "POST":
        form = ToDoForm(request.POST or None)
        if form.is_valid():
            form.save(
                commit=False
            ).user_id = (
                request.user
            )  # this line delay the form form saving and accessing the user_id (user_id - this is the foreign key we created in model) to access the current user and after this i save my form below
            # the commit=False attribute delay my save and then i access my user_id which i created in model earlier then make migrations here i use the foreign key field save the form with use of request.user
            form.save()
            # the below also working as expected
            # formInstance = form.save(commit=False)
            # formInstance.user_id = request.user
            # formInstance.save()
            messages.success(request, ("ToDo's added successfully!"))
        return redirect("toDoList")
    else:
        # toDos = (
        # TodoList.objects.all() # if i use objects.all() it will get all the datas from the ToDo model
        # )  # if we use pagination then u must mention objects.all with paranthesis like this object.all() else we got error, if we dont use pagination then dont need to be mention paranthesis
        toDos = TodoList.objects.filter(
            user_id=request.user
        )  # this filter takes the field as a parameter and the with filed and request value it will the records acccoring to it
        paginationIns = Paginator(
            toDos, 5
        )  # this paginator class accepts two arguments, 1 is which datas to paginate, 2 is page limit
        whichPage = request.GET.get(
            "page"
        )  # here we create url parameters using pagination instance that we created on above line
        toDos = paginationIns.get_page(whichPage)
        datas = {
            "welcome_text": "Warm Welcome from To Do Page!",
            "data": toDos,
        }  # get all objects from model to view, import which to retrieve data with use of objects.all method, this method return data as List datatype
        return render(request, "todo.html", datas)


@login_required
def editToDo(request, todo_id):
    if request.method == "POST":
        todo = TodoList.objects.get(pk=todo_id)
        form = ToDoForm(
            request.POST or None, instance=todo
        )  # this instance will find the requested edit object in db through models
        if form.is_valid():
            form.save()
            messages.success(request, ("ToDo Updated Successfully!"))
            return redirect("toDoList")
    else:
        todo_obj = TodoList.objects.get(pk=todo_id)
        datas = {"data": todo_obj}
        return render(request, "editToDo.html", datas)


@login_required
def completeToDo(request, todo_id):
    toDo = TodoList.objects.get(pk=todo_id)
    if toDo.user_id == request.user:
        if toDo.status == True:
            toDo.status = False
        else:
            toDo.status = True
        toDo.save()
        messages.success(request, ("ToDo Marked as per your Wish!"))
    else:
        messages.error(request, ("Your are not allowed to access this Location!"))
    return redirect("toDoList")


@login_required
def deleteToDo(request, todo_id):
    selectToDo = TodoList.objects.get(pk=todo_id)
    if selectToDo.user_id == request.user:
        if selectToDo.delete():
            messages.success(request, ("ToDo deleted Successfully!"))
    else:
        messages.error(request, ("Your are not allowed to access this Location!"))
        return redirect("toDoList")


@login_required
def taskList(request):
    datas = {"data": "Warm Welcome from Task Page!"}
    return render(request, "task.html", datas)
    # here for the render () it accepts three parameters 1st - request from browser from clientside, 2nd - which html template should render, 3rd - dynamic datas remember it always a form of dictionaries


def contactList(request):
    datas = {"data": "Warm Welcome from Contact Page!"}
    return render(request, "contact.html", datas)


def aboutUs(request):
    datas = {"data": "Warm Welcome from About Page!"}
    return render(request, "about.html", datas)
