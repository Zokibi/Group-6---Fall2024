from django.db import models
from TMS.models import Order, Server, Table
# Create your models here.

class Order(models.Model):
    meal = models.ManyToManyField(Order)
    server = models.ForeignKey(Server, related_name='host', on_delete=models.CASCADE)
    table = models.ForeignKey(Table, related_name='seatTable', on_delete=models.CASCADE)