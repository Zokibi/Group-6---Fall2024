from django.db import models

# Create your database models here.

class EmployeeClockin(models.Model):
    Server = models.CharField(max_length=200)
    clockin = models.BooleanField(default=False)
    
class User(models.Model):
    userID = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

class Table(models.Model):
    tableID = models.CharField(primary_key=True, max_length=30)
    chairs = models.IntegerField
    table_status = models.CharField(max_length=30)

class Order(models.Model):
    orderID = models.CharField(primary_key=True, max_length=30)
    tableID = models.CharField(max_length=30)
    order_status = models.CharField(max_length=30)

class Item(models.Model):
    itemID = models.CharField(primary_key=True, max_length=30)
    itemName = models.CharField(max_length=30)
    price = models.FloatField





