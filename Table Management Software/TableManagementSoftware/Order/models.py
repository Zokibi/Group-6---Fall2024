from django.db import models
from Server.models import serverList
from Table.models import tableNum

# Create your models here.


menuItems = {
    "1": "Cheese Burger",
    "2": "Double Cheese Burger",
    "3": "Steak Burrito",
    "4": "Chicken Burrito",
    "5": "Pepperoni Pizza",
    "6": "Grilled Chicken Salad",
}

class Order(models.Model):
    server = models.CharField(max_length=10, choices=serverList)
    table = models.CharField(max_length=1, choices=tableNum)
    menu = models.CharField(max_length=1, choices=menuItems)
    pass
