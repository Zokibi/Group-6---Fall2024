from django.db import models

# Create your database models here.


class Employees(models.Model):
    employeeList = {
        "1": "Charne Robinson",
        "2": "Jacob Sparks",
        "3": "Daryna Kozlova",
        "4": "Isaiah Dillard",
        "5": "Anthony Gilliam",
    } # list of all the employees for selection
    employeeSelection = models.CharField(max_length=10, choices=employeeList)
    

class MealOrder(models.Model):
    menuOptions = {
        "1": "Cheese Burger",
        "2": "Double Cheese Burger",
        "3": "Steak Burrito",
        "4": "Chicken Burrito",
        "5": "Pepperoni Pizza",
        "6": "Grilled Chicken Salad",
    }
    menuSelection = models.CharField(max_length=1, choices=menuOptions)
    
class Tables(models.Model):
    tableNumbers = {
        "1": "1- 4 seats",
        "2": "2- 4 seats",
        "3": "3- 4 seats",
        "4": "4- 6 seats",
        "5": "5- 6 seats",
        "6": "6- 6 seats",
        "7": "7- 8 seats",
        "8": "8- 8 seats",
    }
    tableSelection = models.CharField(max_length=1, choices=tableNumbers)