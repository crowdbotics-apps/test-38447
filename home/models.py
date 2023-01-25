from django.conf import settings
from django.db import models
class Sales(models.Model):
    'Generated Model'
    price = models.BigIntegerField()
    itemName = models.TextField(null=True,blank=True,)
class Order(models.Model):
    'Generated Model'
    qty = models.SmallIntegerField()
    orderDate = models.DateTimeField(null=True,blank=True,)
    item = models.OneToOneField("home.Sales",on_delete=models.CASCADE,null=True,blank=True,related_name="order_item",)
