from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")
    #return HttpResponse("this is home page")
def about(request):
    return render(request,"about.html")
    #return HttpResponse("this is about page")
def services(request):
    return render(request,"services.html")
    #return HttpResponse("this is my services")
@login_required(login_url='login')
def contect(request):
    return render(request,"contect.html")
    #return HttpResponse("this is my login page")

def signup(request):
    if request.method=='POST':
         uname=request.POST.get('username')
         email=request.POST.get('email')
         pass1=request.POST.get('password1')
         pass2=request.POST.get('password2')
         if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        
         else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
       
    return render(request,"signup.html")
    #return HttpResponse("this is my login page") 

def login1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('contect')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('home')
    #return HttpResponse("this is my login page")   


