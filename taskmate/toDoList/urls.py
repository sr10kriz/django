from django.urls import path
from toDoList import views

urlpatterns = [
    path('',views.toDoList,name='toDoList'),
    path('task/',views.taskList,name='taskList'),
    path('contact/',views.contactList,name='contactUs'),
    path('about/',views.aboutUs,name='aboutUs')
]
# this path methods accepts three parameters
""" 1st - routing url,
    2nd - which views to be processed for the specific url/route
    3rd - name its a super important parameter and mandatory one, whatever the name we provide here is the name we use while using anchor tags with {% url <name>%} - its a jinja2 method usefull in many scenarios refer base template for reference purpose, this will take us to specific routes, see base template file inside root directory for reference purpose... """