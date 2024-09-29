from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"), # will call the home function in views
    path("login/", views.login_view, name="login"), # will call the sign_in_view function in views
    path("signup/", views.sign_up_view, name="signup"), # will call the sign_up_view function in views
    path("about/", views.about_view, name="about")
]