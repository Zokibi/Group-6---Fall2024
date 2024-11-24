from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import UserManager, User
from decimal import Decimal

# Create your database models here.

class User(Abstract)
class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=30,
        choices=[('Host', 'Host'),('Server', 'Server')]
    )
    name = models.CharField(max_length=30, )
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    numTables = models.PositiveIntegerField(editable=True, default=1)

    def __str__(self):
        return self.name
    
    
class Table(models.Model):
    tableID = models.AutoField(primary_key=True)
    shape = models.CharField(max_length=30, choices=(('circle', 'circle'), ('rect', 'rect')), default='rect')
    table_status = models.CharField(max_length=30, choices=(('available', 'Available'), ('occupied', 'Occupied'), ('reserved', 'Reserved')), default='Available')
    guests = models.PositiveIntegerField(editable=True, default=1)
    seats = models.PositiveIntegerField(editable=True, default=1)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, editable=True, on_delete=models.CASCADE)

    def get_employee(self, employee):
        return employee.first_name

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=30, choices=(('Pending', 'Pending'), ('Complete', 'Complete')))

class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    order = models.ManyToManyField(Order, through='OrderItem')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    item_quantity = models.PositiveIntegerField(editable=True, default=1)


