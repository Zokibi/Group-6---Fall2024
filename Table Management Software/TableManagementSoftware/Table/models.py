from django.db import models

# Create your models here.

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

class Table(models.Model):
    tableSelection = models.CharField(max_length=1, choices=tableNum)