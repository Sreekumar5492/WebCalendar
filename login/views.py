from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from web_calendar.forms import userprofileform
from django.contrib.auth.models import User
from django.contrib import messages
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
            messages.add_message(request, messages.ERROR, "Credintials are invalid!.")
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
            user        = User.objects.create_user(username,password=pwd1)
            form        = userprofileform(request.POST)
            form.user   = user
            print form
            if form.is_valid():
                user.save()
                userprofile = form.save(commit=False)
                userprofile.user = user
                userprofile.save()
                return render(request,'login/login.html')
            else:
                return render(request,'login/signup.html')
        else:
            return render(request,'login/signup.html')
    else:
        form=userprofileform()
        args= {'form':form}
    return render(request,'login/signup.html',args)