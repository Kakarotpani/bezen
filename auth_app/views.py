from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')

def register_method(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            registered = True
            messages.success(request, "Registered Successfully !!")
            return HttpResponseRedirect('/login')
        else:
            messages.error(request, "* Invalid data . Try Again !!")
            return HttpResponseRedirect('/register')
    else:
        context = {
            'user_form': UserForm(),
            'registered': registered,
            'list_items': ['1', '2', '3', '4', '5']
        }
    return render(request, 'register.html', context=context)


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
    return HttpResponseRedirect('/login')

@login_required(login_url='/login')
def profile_update(request):
    user = User.objects.get(email= request.user.email)
    profile = UserForm(instance=user)
    if request.method == "POST":
        data = UserForm(request.POST, instance=user)
        if data.is_valid():
            data.save(commit=True)
            messages.success(request, "* Profile Updated successfully .....")
            return HttpResponseRedirect('/profile/update')
        else:
            messages.error(request, "* Invalid data . Try Again !!")
            return HttpResponseRedirect('/profile/update')
    context = {
        'user_form': profile,
    }
    return render(request, 'profile.html', context=context)
