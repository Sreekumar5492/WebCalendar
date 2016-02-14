from django.shortcuts import render ,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from web_calendar.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
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
            arg     = {"login":True,"message":"Success! Logging In.."}             
            return HttpResponse(json.dumps(arg))
#            return redirect('/web_calendar/home/')
        else:
#            messages.add_message(request, messages.ERROR, "Invalid credentials!")
            arg     = {"login":False,"message":"Invalid credentials! Try Again!"}  
            return HttpResponse(json.dumps(arg))
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
#                 messages.add_message(request, messages.ERROR, "Username already exists!")
                 args     = {"status":False,"message":"Username already exists!"} 
                 return HttpResponse(json.dumps(args))
            
            try:
                userp       = userprofile()
                userp.name  = name
                userp.email = email
                userp.user  = user
                userp.save()
                args     = {"status":True,"message":"Success, Now Login!"} 
                return HttpResponse(json.dumps(args))
            except Exception,e:
#                messages.add_message(request, messages.ERROR, "Failed! Try again Later! ")
                args     = {"status":False,"message":"Failed! Try again Later!"} 
                return HttpResponse(json.dumps(args))
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
             