from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # will call the home function in views
    path("login/", views.login_view, name="login"), # will call the sign_in_view function in views
    path("signup/", views.signup_view, name="signup"), # will call the sign_up_view function in views
    path("about/", views.about_view, name="about"),
    path("menu/", views.menu_view, name="menu"),
    path("deleteitem/<int:itemID>", views.delete_item, name="deleteitem"),
    path('logout/', views.logout_view, name="logout"),
    path("restaurant/", views.restaurant_view, name="restaurant"),
    path("table/", views.table_view, name="table"),
    path('deletetable/<int:tableID>', views.delete_table, name='deletetable'),
    path('restaurant-layout/', views.restaurant_layout, name='restaurant_layout'),
]