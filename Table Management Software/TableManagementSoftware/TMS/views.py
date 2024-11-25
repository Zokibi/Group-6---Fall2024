from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from .forms import *

from .models import *


# Create your views here.
def home(request):
    return render(request, "home.html") # renders the login template in templates folder

def login_view(request):
    form = CreateLoginForm()
    
    if request.method == 'POST':
        form = CreateLoginForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Login successful!")
            return redirect("about")
        else:
            messages.info(request, "Incorrect username or password")
            form = CreateLoginForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if form.is_valid():
            login(request, form.save())
            uname = form.cleaned_data.get('username')
            messages.success(request, 'Account created for user ' + uname)
            user = User.objects.get(username=uname)
            if admin:
                user.is_superuser == True
            return redirect("about")
        else:
            if password1 != password2:
                messages.info(request, 'Passwords do not match')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
            form = CreateUserForm()
    return render(request, 'sign_up.html', {'form':form})  # Render sign-up page on GET request

def logout_view(request):
    logout(request)
    return redirect('home')

def about_view(request):
    return render(request, "about.html")

def menu_view(request):
    form = AddMenuItem()
    item  = Item.objects.all()

    if request.method =='POST':
        form = AddMenuItem(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('itemName')
            messages.success(request, name + ' added to the menu successfully')
            return redirect(request.path)
    return render(request, "menu.html", {'item': item, 'form': form})

def restaurant_view(request):
    form = SaveRestaurantProfile()
    restaurants = Restaurant.objects.all()

    if request.method == 'POST':
        form = SaveRestaurantProfile(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, name + ' successfully added')
            return redirect(request.path)
    return render(request, 'restaurant.html', {'restaurants': restaurants, 'form': form})

def table_view(request):
    tables = Table.objects.all()
    return render(request, 'tables.html', {'tables': tables})

def restaurant_layout(request):
    return render(request, 'restaurant_layout.html')