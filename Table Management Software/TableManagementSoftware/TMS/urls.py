from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # will call the home function in views
    path("login/", views.login_view, name="login"), # will call the sign_in_view function in views
    path("signup/", views.signup_view, name="signup"), # will call the sign_up_view function in views
    path("about/", views.about_view, name="about"),
    path("menu/", views.menu_view, name="menu"),
    path('logout/', views.logout_view, name="logout"),
    path("restaurant/", views.restaurant_view, name="restaurant"),
    path("table/", views.table_view, name="table"),
    path('layout/', views.layout_view, name="layout"),
    path('update_layout/<str:pk>', views.update_table, name="update_table")
]