from django.shortcuts import render ,redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from web_calendar.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def login(request):
    return render(request,'login/login.html')

def loginuser(request):
    if request.POST:
        username    = request.POST['username']
        pwd         = request.POST['password']
        user        = authenticate(username=username,password=pwd)
        if user is not None:
            auth_login(request, user)
            return redirect('/web_calendar/home/')
        else:
            messages.add_message(request, messages.ERROR, "Invalid credentials!")
            return render(request,'login/login.html')
def logoutuser(request):
    logout(request)
    return render(request,'login/login.html')

def signup(request):
    args = {}
    if request.POST:
        pwd1      = request.POST['password1']
        pwd2      = request.POST['password2']
        if pwd1 == pwd2:
            username    = request.POST['username']
            name        = request.POST['name']
            email       = request.POST['email']
            try:
                user        = User.objects.create_user(username,password=pwd1)
                user.save()
            except:
                 messages.add_message(request, messages.ERROR, "Username already exists!")
                 args = {'name':name,
                         'email':email
                        }
                 return render(request,'login/signup.html',args)
            
            try:
                userp       = userprofile()
                userp.name  = name
                userp.email = email
                userp.user  = user
                userp.save()
                return render(request,'login/login.html')
            except Exception,e:
                messages.add_message(request, messages.ERROR, "Failed! Try again Later! ")
                return render(request,'login/signup.html')
        else:
            return render(request,'login/signup.html')
    return render(request,'login/signup.html',args)

@csrf_exempt
def user_available(request):
     if request.POST:
        user   = request.POST['username']
        if User.objects.filter(username=user).exists():
             response = 'Username already Exists!'
        else:
             response = 'true'
        return JsonResponse(response,safe=False)
             