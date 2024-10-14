from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

# Create your database models here.

class EmployeeClockin(models.Model):
    Server = models.CharField(max_length=200)
    clockin = models.BooleanField(default=False)
    
class Table(models.Model):
    tableID = models.AutoField(primary_key=True)
    chairs = models.PositiveIntegerField(editable=True, default=0)
    table_status = models.CharField(max_length=30)

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    Table.tableID
    order_status = models.CharField(max_length=30)

class TableOrder(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    order = models.ManyToManyField(Order, through='OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    item_quantity = models.IntegerField





