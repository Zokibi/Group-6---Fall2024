from django.db import models
from TMS.models import tableNum, employeeList, Order

# Create your models here.

class Table(models.Model):
    table = models.CharField(max_length=5, choices=tableNum)
    server = models.CharField(max_length=5, choices=employeeList)
    orders = models.ManyToManyField(Order)