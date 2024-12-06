from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import UserManager, User
from decimal import Decimal

# Create your database models here.
class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    numTables = models.PositiveIntegerField(editable=True, default=0)

    def __str__(self):
        return self.name
     
    
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=30,
        choices=[('Host', 'Host'),('Server', 'Server')],
        default='Server'
    )

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    def getRole(self):
        return self.role
    
class Table(models.Model):
    tableID = models.AutoField(primary_key=True)
    shape = models.CharField(max_length=30, choices=(('circle', 'Circle'), ('rect', 'Rectangle')), default='Rectangle')
    table_status = models.CharField(max_length=30, choices=(('available', 'Available'), ('occupied', 'Occupied'), ('reserved', 'Reserved')), default='Available')
    guests = models.PositiveIntegerField(editable=True, default=0)
    seats = models.PositiveIntegerField(editable=True, default=1)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, editable=True, on_delete=models.CASCADE, null=True)

    def get_employee(self):
        return f'{self.employee.user.first_name} {self.employee.user.last_name}'
    
    def __str__(self):
        return self.restaurant.name + ': Table ' + str(self.tableID)

class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=30, choices=(('Pending', 'Pending'), ('Complete', 'Complete')))
    
    def __str__(self) -> str:
        return f"{self.table.restaurant} Table {self.table.tableID} Order Status: {self.order_status}"

class Item(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    order = models.ManyToManyField(Order, through='OrderItem')

    def __str__(self):
        return self.itemName

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    item_quantity = models.PositiveIntegerField(editable=True, default=1)

    def __str__(self):
        return f"Order #: {self.order.orderID}, Item: {self.item}, Quantity: {self.item_quantity}"


