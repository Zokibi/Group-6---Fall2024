from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

# Create your views here.
def home(request):
    return render(request, "login.html") # renders the login template in templates folder

def login_view(request):
    if request.method == 'POST':
        # Get username and password from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in and redirect to the home page (or wherever you like)
            login(request, user)
            return redirect('home')  # 'home' should be the name of the URL route for the home page
        else:
            # Invalid credentials, show an error message
            messages.error(request, 'Invalid username or password.')

    # If GET request or failed login, re-render the login page
    return render(request, 'login.html')  # 'login.html' is your login template

def signup_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for user ' + user)

        # # Log the user in and redirect to home page
        # login(request, user)
        # return redirect('home')  # Adjust this to redirect to your desired page

    return render(request, 'sign_up.html', {'form':form})  # Render sign-up page on GET request 

def about_view(request):
    return render(request, "about.html")