from django.urls import path
from usersApp import views
from django.contrib.auth import views as auth_views
# for login & login and authentication funtionality, django comes up with default tools, as you see  in the register form, now for login & logout we use class based views that are available in django contrib auth - remember its a predined login & logout functionalities, we utilize it NOTEE: it pretty secure & one good feature in django

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'), # why we need to mention template_name = login.html this is how we call template files using class based views, any doubts then go & watch login & logout in Django udemy
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'),name='logout')
]
