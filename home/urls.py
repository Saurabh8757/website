from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contect",views.contect,name='contect'),
    path("login",views.login1,name='login'),
    path("signup",views.signup,name='singup'),
    path("logout",views.logoutpage,name='logout'),
]
