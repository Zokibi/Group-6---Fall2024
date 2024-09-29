from django.contrib import admin
from .models import MealOrder, Employees, Tables

# Register your models here.
admin.site.register(MealOrder)
admin.site.register(Employees)
admin.site.register(Tables)