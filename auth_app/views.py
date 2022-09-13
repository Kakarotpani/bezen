from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

""" def register(request):
    registered = False
    if request.method == 'POST':
        profileForm = profileForm(request.POST)        
        if user_form.is_valid() and profile_form.is_valid():             
            user = user_form.save()
            user.set_password(user.password)
            profile.user = user
            profile.save()
            registered = True
            messages.success(request, "* Successfully Registered as an Applicant .......")
            return HttpResponseRedirect('/login')
        else:
            messages.error(request,"* Invalid data . Try Again !!")
            return HttpResponseRedirect('/register/seeker')
    else:
        context = {
            'user_form' : User_Form(),
            'registered' : registered 
        }        
    return render(request, 'seeker_register.html', context = context)

def login_method(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)   
                messages.success(request, "* Logged in successful !!")
                return HttpResponseRedirect('/')
            else:
                messages.error(request, "User doesn't exist.")
                return HttpResponseRedirect('/login')
        else:
            messages.warning(request, "* INVALID CREDENTIALS !!")
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html')


@login_required
def logout_method(request):
    logout(request)
    messages.success(request, "* Successfully Logged out !!")
    return HttpResponseRedirect('/login') """
