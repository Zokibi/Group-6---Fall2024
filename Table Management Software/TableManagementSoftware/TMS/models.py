from django.db import models


# Create your database models here.

employeeList = {
    "100": "Charne Robinson",
    "200": "Jacob Sparks",
    "300": "Daryna Kozlova",
    "400": "Isaiah Dillard",
    "500": "Anthony Gilliam",  
}

tableNum = {
    "1": "1- 4 seats",
    "2": "2- 4 seats",
    "3": "3- 4 seats",
    "4": "4- 6 seats",
    "5": "5- 6 seats",
    "6": "6- 6 seats",
    "7": "7- 8 seats",
    "8": "8- 8 seats",
}

menuItems = {
    "1": "Cheese Burger",
    "2": "Double Cheese Burger",
    "3": "Steak Burrito",
    "4": "Chicken Burrito",
    "5": "Pepperoni Pizza",
    "6": "Grilled Chicken Salad",
}

class Server(models.Model):
    server = models.CharField(max_length=5, choices=employeeList)
    pass

class Table(models.Model):
    table = models.CharField(max_length=1, choices=tableNum)
    pass

class Order(models.Model):
    meal = models.CharField(max_length=1, choices=menuItems)
    pass