from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "login.html") # renders the login template in templates folder

def sign_in_view(request):
    return render(request, "sign_in.html") # renders the sign_in template in templates folder

def sign_up_view(request):
    return render(request, "sign_up.html") #renders the sign_up template in templates folder

def about_view(request):
    return render(request, "about.html")