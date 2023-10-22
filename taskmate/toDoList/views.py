from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def toDoList(request):
    return HttpResponse('Your To Do\'s are Here, Glad to Have you here!')

def taskList(request):
    datas = {'data':'haha ha Your pending tasks are here!'}
    return render(request,'task.html',datas)
    # here for the render () it accepts three parameters 1st - request from browser from clientside, 2nd - which html template should render, 3rd - dynamic datas remember it always a form of dictionaries
