from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def toDoList(request):
#     return HttpResponse('Your To Do\'s are Here, Glad to Have you here!')

def toDoList(request):
    datas = {'data': 'Warm Welcome from To Do Page!'}
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

# this for reference purpose, <todo.html> jinja2 stuffs
# we get dynamic datas from views to templates using jinja2 method, jinja2 used to iterate datas, extendinng templates (which means template inheritance), integrating links refer google to know more about jinja2
# {%comment %} {% extends "footer.html" %} - in template we may able to inherit single template in another template file {%endcomment %} 
# {% comment %} whatever we give inside the block endblock it will replace the block endblock in the base template file - here we use it for title of the webpage, but we may able to use block endblock with any kind of stuff {%endcomment %} 