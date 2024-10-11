from django.db import models
from TMS.models import employeeList, Table, Order

# Create your models here.

class Server(models.Model):
    server = models.CharField(max_length=5, choices=employeeList)
    orders = models.ManyToManyField(Order)
    tables = models.ManyToManyField(Table)