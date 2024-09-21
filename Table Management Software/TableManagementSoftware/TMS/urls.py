from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # will call the home function in views
    path("signin/", views.sign_in_view, name="signin"), # will call the sign_in_view function in views
    path("signup/", views.sign_up_view, name="signup") # will call the sign_up_view function in views
]