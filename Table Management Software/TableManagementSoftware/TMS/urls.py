from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # will call the home function in views
    path("login/", views.login_view, name="login"), # will call the sign_in_view function in views
    path("signup/", views.signup_view, name="signup"), # will call the sign_up_view function in views
    path("about/", views.about_view, name="about"), # calls the about_view to display about page
    path("menu/", views.menu_view, name="menu"), # calls the menu_view to display menu page
    path("deleteitem/<int:itemID>", views.delete_item, name="deleteitem"), # calls delete_item to delete item from database.
    path('logout/', views.logout_view, name="logout"), # calls logout_view to logout current user
    path("restaurant/", views.restaurant_view, name="restaurant"), # calls restaurant_view to display the restaurant page
    path("table/", views.table_view, name="table"), # calls table_view to display the table page
    path('deletetable/<int:tableID>', views.delete_table, name='deletetable'), # calls delete_table to delete a specific restaurant table based on its ID
    path('layout/', views.restaurant_layout, name='layout'), # calls restaurant_layout to display the GUI for the floor plan
    path('admin-login/', admin.site.urls), # gives access to the admin site 
]