from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    datas = {'data': 'Welcome to TaskMate!'}
    return render(request,'home.html',datas)