from django.db import models

# Create your database models here.

class EmployeeClockin(models.Model):
    Server = models.CharField(max_length=200)
    clockin = models.BooleanField(default=False)
    