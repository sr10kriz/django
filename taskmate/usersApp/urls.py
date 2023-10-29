from django.urls import path
from usersApp import views

urlpatterns = [
    path('register/',views.register,name='register')
]
