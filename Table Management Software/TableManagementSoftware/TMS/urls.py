from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home") # will call the home function in views
]