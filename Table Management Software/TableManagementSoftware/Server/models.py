from django.db import models

# Create your models here.

serverList = {
    "100": "Charne Robinson",
    "200": "Jacob Sparks",
    "300": "Daryna Kozlova",
    "400": "Isaiah Dillard",
    "500": "Anthony Gilliam",
}

class Server(models.Model):
    employeeSelection = models.CharField(max_length=10, choices=serverList)
    pass