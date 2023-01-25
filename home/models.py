from django.conf import settings
from django.db import models
class Sales(models.Model):
    'Generated Model'
    salesDate = models.DateTimeField(auto_now=True,)
    qty = models.SmallIntegerField()
    price = models.BigIntegerField()
