from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import serializers


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

@receiver(post_save, sender=User)
def create_emploeyee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

def signup_view(request):
    form = CreateUserForm()
    form2 = EmployeeForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = EmployeeForm(request.POST)

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if form.is_valid() and form2.is_valid():
            login(request, form.save())
            uname = form.cleaned_data.get('username')
            messages.success(request, 'Account created for user ' + uname)
        else:
            if password1 != password2:
                messages.info(request, 'Passwords do not match')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
            form = CreateUserForm()
    return render(request, 'sign_up.html', {'form':form, 'form2': form2})  # Render sign-up page on GET request

def logout_view(request):
    logout(request)
    return redirect('home')

def about_view(request):
    return render(request, "about.html")

@login_required
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

def delete_item(request, itemID):
    Item.objects.get(itemID = itemID).delete()
    return redirect(menu_view)

@login_required
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

@login_required
def table_view(request):
    form = AddTable()
    tables = Table.objects.all()

    if request.method =='POST':
        form = AddTable(request.POST)

        id = request.POST['restaurant']
        r = Restaurant.objects.get(id=id)
        specific_tables = Table.objects.filter(restaurant = id)
        
        if form.is_valid and specific_tables.count() <= r.numTables:
            form.save()
            r.numTables = specific_tables.count()
            r.save()
            return redirect(request.path)
    return render(request, 'tables.html', {'tables': tables, 'form': form})

def delete_table(request, tableID):
    Table.objects.get(tableID = tableID).delete()
    return redirect(table_view)

@login_required
def restaurant_layout(request):
    tables = list(Table.objects.values())
    restaurants = list(Restaurant.objects.values())
    employees = list(Employee.objects.values())
    users = list(User.objects.values())

    context = {'restaurants': restaurants, 'tables': tables, 'employees': employees, 'users': users}
    return render(request, 'restaurant_layout.html', context)

