from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm # by default django comes up with regsitration forms, we utilize them
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,('User Created Successfully.'))
            return redirect('register')
        else:
            messages.error(request,('Failed to create User, please Try again!'))
            return redirect('register')
    else:
        register_form = UserCreationForm()
        datas = {'data':'Welcome to Taskmate!', 'register_form': register_form}
        return render(request,'register.html',datas)
