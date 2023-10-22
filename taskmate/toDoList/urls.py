from django.urls import path
from toDoList import views

urlpatterns = [
    path('',views.toDoList,name='toDoList'),
    path('pending-task/',views.taskList,name='taskList')
]
