from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login

from .forms import CreateUserForm, CreateLoginForm, SaveRestaurantProfile

from .models import *


# Create your views here.
def home(request):
    return render(request, "login.html") # renders the login template in templates folder

def login_view(request):
    form = CreateLoginForm()
    
    if request.method == 'POST':
        form = CreateLoginForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("about")
        else:
            form = CreateLoginForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for user ' + user)
            return redirect("about")
        else:
            form = CreateUserForm()
    return render(request, 'sign_up.html', {'form':form})  # Render sign-up page on GET request 

def about_view(request):
    return render(request, "about.html")

def menu_view(request):
    item  = Item.objects.all()
    return render(request, "menu.html", {'item': item})

def profile_view(request):
    form = SaveRestaurantProfile()
    restuarants = Restaurant.objects.all()
    return render(request, 'profile.html', {'restaurants': restuarants})