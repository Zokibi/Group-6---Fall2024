from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)

admin.site.register(Table)

admin.site.register(Order)

admin.site.register(Item)

admin.site.register(OrderItem)

admin.site.register(Restaurant)