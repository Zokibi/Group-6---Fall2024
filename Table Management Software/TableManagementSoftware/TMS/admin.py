from django.contrib import admin
from .models import Order, Server, Table

# Register your models here.
admin.site.register(Order)
admin.site.register(Server)
admin.site.register(Table)